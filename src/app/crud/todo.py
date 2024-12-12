from sqlmodel import Session, select
from src.app.models.todo import Todo
from src.app.core.db.database import engine
from sqlalchemy import MetaData, Table, select

def get_all_todos(session: Session):
    return session.exec(select(Todo)).all()

def get_all_todos_users(session: Session):
    v = Table('todo_users_views', MetaData(), autoload_with=engine)
    with Session(engine) as session:  
        vendas = session.exec(v.select())
        lista = []
        for row in vendas:
            print(row)
        return lista