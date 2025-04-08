from datetime import date
from modules.common.schema import ExtensionSchema
from pydantic import Field

class TaskDetail(ExtensionSchema):
  id: int
  task_id: int = Field(description="タスクヘッダID")
  title: str = Field(description="タイトル")
  priority_id: int = Field("優先度ID")
  status_id: int = Field("ステータスID")
  staff_id: int = Field(description="従業員ID")
  created_at: date = Field(description="作成日時")
  created_by: int = Field(description="作成担当者")
  modified_at: date = Field(description="更新日時")
  modified_by: int = Field(description="更新担当者")
  start_date: date = Field(description="タスク開始日")
  end_date: date = Field(description="タスク締切日")
  is_done: bool = Field(description="完了フラグ")
  active: bool = Field(description="アクティブ")

class TaskDetailCreateSchema(ExtensionSchema):
  title: str = Field(description="タイトル")
  priority_id: int = Field("優先度ID")
  status_id: int = Field("ステータスID")
  staff_id: int = Field(description="従業員ID")
  start_date: date = Field(description="タスク開始日")
  end_date: date = Field(description="タスク締切日")
  active: bool = Field(description="アクティブ",default=True)