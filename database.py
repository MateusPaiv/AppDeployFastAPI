from sqlmodel import SQLModel, create_engine
import os

environment = os.getenv("ENVIRONMENT", "development")

DATABASE_URL = "postgresql://postgres.gukfcizmqwjthzueiyqm:QhXXjU3OAeDEDgxQ@aws-0-sa-east-1.pooler.supabase.com:6543/postgres" if environment == "development" else "postgresql://postgres.qylcbshcbfcfnvvtsmmo:lumy3099@aws-0-sa-east-1.pooler.supabase.com:6543/postgres"

try:
    engine = create_engine(DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
