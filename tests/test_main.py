
# import pytest
# import pytest_asyncio
# from httpx import AsyncClient,ASGITransport
# from peewee import *
# import starlette.status

# from api.models.task import Task,Done
# from api.db import get_db
# from api.main import app

# db = PostgresqlDatabase("task_data",user="kaneko",password="goldsilver",port=5432,host="postgresql")

# @pytest_asyncio.fixture
# async def async_client() -> AsyncClient:
#     db.drop_tables([Task,Done])
#     db.create_tables([Task,Done])
#     print("aaa")
#     async def get_test_db():
#         print("bbb")
#         try:
#             db.connect()
#             yield
#         finally:
#             db.close()
#         print("ccc")

#     app.dependency_overrides[get_db] = get_test_db

#     async with AsyncClient(transport=ASGITransport(app=app),base_url="http://test") as client:
#         yield client


# #AC()


# @pytest.mark.asyncio
# async def test_create_and_read(async_client):
#     #print(async_client)
#     response = await async_client.post("/tasks", json={"title": "テストタスク"})
#     assert response.status_code == starlette.status.HTTP_200_OK
#     response_obj = response.json()
#     assert response_obj["title"] == "テストタスク"

#     response = await async_client.get("/tasks")
#     assert response.status_code == starlette.status.HTTP_200_OK
#     response_obj = response.json()
#     assert len(response_obj) == 1
#     assert response_obj[0]["title"] == "テストタスク"
#     assert response_obj[0]["done"] is False



# @pytest.mark.asyncio
# async def test_done_flag(async_client):
#     response = await async_client.post(
#         "/tasks", json={"title": "テストタスク2"}
#     )
#     assert response.status_code == starlette.status.HTTP_200_OK
#     response_obj = response.json()
#     assert response_obj["title"] == "テストタスク2"

#     # 完了フラグを立てる
#     response = await async_client.put("/tasks/1/done")
#     assert response.status_code == starlette.status.HTTP_200_OK

#     # 既に完了フラグが立っているので400を返却
#     response = await async_client.put("/tasks/1/done")
#     assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST

#     # 完了フラグを外す
#     response = await async_client.delete("/tasks/1/done")
#     assert response.status_code == starlette.status.HTTP_200_OK

#     # 既に完了フラグが外れているので404を返却
#     response = await async_client.delete("/tasks/1/done")
#     assert response.status_code == starlette.status.HTTP_404_NOT_FOUND




