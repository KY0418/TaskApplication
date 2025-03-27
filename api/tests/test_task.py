import pytest
from peewee import PostgresqlDatabase
from fastapi.testclient import TestClient
from main import app
from modules.task.model import Task
from modules.task.schemas import TaskCreate, TaskCreateResponse
from modules.task.api import create_task, update_task, delete_task
from modules.status.models import Status
from modules.importance.models import Priority
from modules.staff.models import Staff
import config as config

db = PostgresqlDatabase(
    config.DB,
    user=config.DB_USER,
    password=config.DB_PASS,
    port=config.DB_PORT,
    host=config.DB_HOST,
)

client = TestClient(app)


def initialize_table_data():
    importance = [
        "重要度高、緊急度高",
        "重要度高、緊急度低",
        "重要度低、緊急度高",
        "重要度低、緊急度低",
    ]
    status = ["未着手", "進行中"]
    for i in importance:
        priority_table = Priority(importance=i)
        priority_table.save()

    for i in status:
        status_table = Status(status=i)
        status_table.save()


@pytest.fixture
async def db_connect():
    db.drop_tables([Task, Status, Staff, Priority])
    db.create_tables([Task, Status, Staff, Priority])
    initialize_table_data()
    try:
        db.connect()
        yield
    finally:
        db.close()


@pytest.fixture
def make_post_data() -> TaskCreate:
    post_data = TaskCreate(
        title="nuwa-",
        status_id=2,
        category="未着手",
        staff_id="000001",
        priority_id=2,
        start_date="2024-04-04",
    )
    return post_data


@pytest.fixture
def make_put_data() -> TaskCreate:
    put_data = TaskCreate(
        title="sawagooo",
        status_id=3,
        category="未着手",
        staff_id="000003",
        priority_id=2,
        start_date="2024-04-07",
    )
    return put_data


@pytest.fixture
def make_response_data():
    response_data = Task()
    return response_data


# post関数テスト
@pytest.mark.asyncio
async def test_post_task(make_post_data, make_response_data):
    make_response_data = await create_task(task_body=make_post_data, db=db)
    print(make_response_data, "response")
    assert make_response_data.title == "nuwa-"
    assert make_response_data.staff_id == "000001"
    assert make_response_data.category == "未着手"
    assert make_response_data.priority_id == 2
    assert make_response_data.start_date == "2024-04-04"
    assert make_response_data.status_id == 2


# put関数テスト
@pytest.mark.asyncio
async def test_put_task(make_response_data, make_put_data):
    make_response_data = await update_task(task_id=86, task_body=make_put_data, db=db)
    assert make_response_data.title == make_put_data.title


# delete関数テスト
@pytest.mark.asyncio
async def test_delete_task():
    result = await delete_task(86, db=db)
    assert result == True


# API　getテスト
def test_get_task():
    response = client.get(url=f"{config.BASE_URL}tasks")

    assert response.status_code == 200
