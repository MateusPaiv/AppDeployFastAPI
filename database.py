from sqlmodel import SQLModel, create_engine
import os

DATABASE_URL = os.getenv(
    "DB_URL_PROD" if os.getenv("ENVIRONMENT", "production") != "development" else "DB_URL_DEV"
)
try:
    engine = create_engine(DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)
        
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
