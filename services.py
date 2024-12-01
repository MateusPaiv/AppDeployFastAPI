from sqlmodel import Session, select
from models import Produto
from database import engine

def insert(nome, valor): 
    with Session(engine) as session:
        produto = Produto(nome=nome, valor=valor)
        session.add(produto)
        session.commit()
        session.refresh(produto) 
        return produto


def select():
    with Session(engine) as session:
        search = select(Produto)
        produtos = session.exec(search).all()
        print(produtos)
        return produtos