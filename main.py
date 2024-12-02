from fastapi import FastAPI
from services import select_produtos
from sqladmin import Admin, ModelView
from database import engine
from models import Produto, Sale
import uvicorn
import os


environment = os.getenv("ENVIRONMENT", "production")
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
    produtos = select_produtos()
    print(produtos)
    return produtos

@app.get("/")
def home():
    if environment == "development":
        return {"message": "Running in development mode"}
    else:
        return {"message": "Running in production mode"}
    
admin.add_view(Produto)
admin.add_view(Sale)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)