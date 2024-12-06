from fastapi import APIRouter, Depends, HTTPException, Header
from sqlmodel import Session
from app.database import engine
from app.crud.todo import get_all_todos
from app.models.todo import Todo
from app.schemas.todo import TodoRead
from app.utils import auth

router = APIRouter(prefix="/todos", tags=["Todos"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/", response_model=list[TodoRead])
def read_todos(session: Session = Depends(get_session)):
    return get_all_todos(session)

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Hero not found")
    return todo

@router.post("/", response_model=TodoRead)
def create_new_todo(todo: Todo, session: Session = Depends(get_session), authorization: str = Header(default=None)):
    if not auth.is_authenticated(authorization):
        raise HTTPException(status_code=401,
                            detail="Authentication credentials were not provided")
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.patch("/{hero_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: Todo):
    with Session(engine) as session:
        db_todo = session.get(Todo, todo_id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Hero not found")
        todo_data = todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return db_todo