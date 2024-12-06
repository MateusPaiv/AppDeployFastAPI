from typing import Optional
from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str
    is_completed: Optional[bool] = False

class TodoRead(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id: int

class TodoView(BaseModel):
    todo_title: str
    todo_description: str
    todo_is_completed: bool
    user_id: int
    user_name: str