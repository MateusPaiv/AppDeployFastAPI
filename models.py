from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class Produto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    valor: float

    # Relacionamento com Sale
    sales: List["Sale"] = Relationship(back_populates="produto")

class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    total: float

    # Chave estrangeira que aponta para Produto
    produto_id: Optional[int] = Field(default=None, foreign_key="produto.id")

    # Relacionamento com Produto
    produto: Optional[Produto] = Relationship(back_populates="sales")

    