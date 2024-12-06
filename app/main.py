from fastapi import FastAPI, Header, HTTPException
import uvicorn
import os
from sqladmin import Admin, ModelView
from app.database import engine
from app.models.todo import Todo, User
from fastapi.middleware.cors import CORSMiddleware
from app.routers import todo

environment = os.getenv("ENVIRONMENT", "development")
app = FastAPI(title="TODO API", version="1.0.0")

app.include_router(todo.router)
origins = [
    "http://localhost",
    "http://localhost:62081",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Running in production mode"} if environment == "production" else {"message": "Running in development mode"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    

# class VendasAll(ModelView, model=VendasAll):
#     vendas = view_vendas()
#     lista = []
#     colunas = [
#         "produto_nome",
#         "produto_valor",
#         "produto_descricao",
#         "venda_total",
#         "cliente_nome",
#         "cliente_idade",
#     ]

#     for row in vendas:
#         lista.append(dict(zip(colunas, row)))
#     print(lista)
#     column_list = lista
    
# @app.get("/produtos")
# def list_produtos(authorization: str = Header(default=None)):
#     if authorization is None:
#         return {"error": "Authorization header missing"}
    
#     if not is_authenticated(authorization):
#         return {"error": "Unauthorized"}
    
#     produtos = select_produtos()
#     return produtos

# @app.get("/vendas")
# def lista_vendas(authorization: str = Header(default=None)):
#     if authorization is None:
#         return {"error": "Authorization header missing"}
#     if not is_authenticated(authorization):
#         return {"error": "Unauthorized"}
    
#     vendas = select_vendas()
#     return vendas
    

admin = Admin(app, engine)

class Todo(ModelView, model=Todo):
    column_list = [Todo.title, Todo.description]

class User(ModelView, model=User):
    can_delete = False
    can_edit = False
    column_list = ('user', 'todo')
    
admin.add_view(Todo)
admin.add_view(User)