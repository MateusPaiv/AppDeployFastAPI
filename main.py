from fastapi import FastAPI, Header, HTTPException
from services import select_produtos, select_vendas
from sqladmin import Admin, ModelView
from database import engine
from models import Produto, Sale, Customer
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
import jwt

jwt_secret = "bUqIEakocsDAsGLQ0hhkLDSulcmChoCjqSTtPeIno8kwsscgf3BmdV/Xwl6oZIZuyG77x6jP3Zeci93mVcNz4g==" 

environment = os.getenv("ENVIRONMENT", "development")
app = FastAPI()
admin = Admin(app, engine)

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


class Produto(ModelView, model=Produto):
    column_list = [Produto.id, Produto.nome, Produto.valor]
    can_delete = False
    can_edit = False

class Customer(ModelView, model=Customer):
    column_list = [Customer.name, Customer.age]
    can_delete = False
    can_edit = False
    
    
class Sale(ModelView, model=Sale):
    can_delete = False
    can_edit = False
    column_list = ('total', 'produto','customer')
    
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
    
@app.get("/produtos")
def list_produtos(authorization: str = Header(default=None)):
    if authorization is None:
        return {"error": "Authorization header missing"}
    
    if not is_authenticated(authorization):
        return {"error": "Unauthorized"}
    
    produtos = select_produtos()
    return produtos

@app.get("/vendas")
def lista_vendas(authorization: str = Header(default=None)):
    if authorization is None:
        return {"error": "Authorization header missing"}
    if not is_authenticated(authorization):
        return {"error": "Unauthorized"}
    
    vendas = select_vendas()
    return vendas
    
def is_authenticated(authorization: str):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header format")
    token = authorization.split(" ")[1]
    
    try:
        decoded_token = jwt.decode(token, jwt_secret , algorithms=["HS256"], audience="authenticated")
        isAuth = decoded_token['aud'] == 'authenticated'
        return isAuth
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/")
def home():
    return {"message": "Running in production mode"} if environment == "production" else {"message": "Running in development mode"}
    
admin.add_view(Produto)
admin.add_view(Sale)
admin.add_view(Customer)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)