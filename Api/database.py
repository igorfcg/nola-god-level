from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#não estou usando dotenv para melhor vizualização do código



# Pegando variáveis do ambiente ou valores padrão
POSTGRES_USER = os.getenv("POSTGRES_USER", "challenge")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "challenge_2024")
POSTGRES_DB = os.getenv("POSTGRES_DB", "challenge_db")
POSTGRES_HOST = "localhost"     #((os.getenv("POSTGRES_HOST", "postgres")))  # nome do serviço no docker-compose
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
