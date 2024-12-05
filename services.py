from sqlmodel import Session, select
from models import Produto, Customer
from database import engine
from database import engine
from sqlalchemy import MetaData, Table, select


def insert(nome, age): 
    with Session(engine) as session:
        customer = Customer(name=nome, age=age)
        session.add(customer)
        session.commit()
        session.refresh(customer) 
        return customer


def select_produtos():
    with Session(engine) as session:
        search = select(Produto)
        produtos = session.exec(search).all()
        print(produtos)
        return produtos
    
    
def select_vendas():
    v = Table('vendas_view', MetaData(), autoload_with=engine)
    with Session(engine) as session:  
        vendas = session.exec(v.select())
        lista = []
        for row in vendas:
            lista.append(row)
        
        print(lista)
        return lista