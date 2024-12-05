from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship, Session
from pydantic import BaseModel, UUID4
import uuid
# from sqlalchemy.sql import text
# from sqlalchemy_views import CreateView

class Produto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    valor: float
    descricao: str
    sales: List["Sale"] = Relationship(back_populates="produto")
    
class Customer(SQLModel, table=True):
    id: Optional[UUID4] = Field(default_factory=uuid.uuid4, nullable=False,primary_key=True)
    name: str
    age: int
    sales: List["Sale"] = Relationship(back_populates="customer") 

class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: float
    produto_id: Optional[int] = Field(default=None, foreign_key="produto.id")
    customer_id: Optional[UUID4] = Field(default=None, foreign_key="customer.id")
    
    produto: Optional[Produto] = Relationship(back_populates="sales")
    customer: Optional[Customer] = Relationship(back_populates="sales")
    

# view = Table('vendas_view', MetaData())
# definition = text("""SELECT 
#                     p.nome AS produto_nome,
#                     p.valor AS produto_valor,
#                     p.descricao AS produto_descricao,
#                     s.total AS venda_total,
#                     c.name AS cliente_nome,
#                     c.age AS cliente_idade
#                 FROM 
#                     produto p
#                 JOIN 
#                     sale s ON p.id = s.produto_id
#                 JOIN 
#                     customer c ON s.customer_id = c.id;""")
# create_view = CreateView(view, definition, or_replace=True)
# with Session(engine) as session:
#     session.exec(create_view)
#     session.commit()