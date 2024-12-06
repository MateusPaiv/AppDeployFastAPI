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
