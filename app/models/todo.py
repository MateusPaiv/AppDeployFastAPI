from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
import uuid 


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    auth_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    email: str
    
    todos: List["Todo"] = Relationship(back_populates="user")
    
class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    is_completed: bool = False
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="todos")