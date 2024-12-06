from sqlmodel import Session, select
from app.models.todo import Todo

def get_all_todos(session: Session):
    return session.exec(select(Todo)).all()


