from fastapi import FastAPI
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
    column_list = [Todo.title, Todo.description, Todo.is_completed, Todo.user_id]

class User(ModelView, model=User):
    can_delete = False
    can_edit = False
    column_list = [User.name, User.email]
    
admin.add_view(Todo)
admin.add_view(User)