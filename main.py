from fastapi import FastAPI
from services import insert, select
from sqladmin import Admin, ModelView
from database import engine
from models import Produto, Sale
import uvicorn

app = FastAPI()
admin = Admin(app, engine)

class Produto(ModelView, model=Produto):
    column_list = [Produto.id, Produto.nome]
    can_delete = False
    can_edit = False

class Sale(ModelView, model=Sale):
    can_delete = False
    can_edit = False
    column_list = ('total', 'produto')

@app.get("/produtos")
def list_produtos():
    produtos = select()
    print(produtos)
    return produtos

# @app.post("/produto", response_model=Produto)
# def save_product(produto: Produto):
#     novo_produto = insert(nome=produto.nome, valor=produto.valor)
#     return {"id": novo_produto.id, "nome": novo_produto.nome, "valor": novo_produto.valor}
    
admin.add_view(Produto)
admin.add_view(Sale)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)