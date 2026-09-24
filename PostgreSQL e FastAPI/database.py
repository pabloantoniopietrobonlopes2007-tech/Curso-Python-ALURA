from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost/escola"

engine = create_engine(DATABASE_URL) # comunica o banco de dados com o FastAPI
SessionLocal = sessionmaker(bind=engine) # cria conexão temporaria com o banco de dados

Base = declarative_base() # cria as entidades