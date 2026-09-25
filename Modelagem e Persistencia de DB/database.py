from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/db_escola'

def criar_banco():
    url_admin = 'postgresql://postgres:postgres@localhost:5432/postgres'
    engine_admin = create_engine(url_admin, isolation_level="AUTOCOMMIT")
    with engine_admin.connect() as conn:
        existe = conn.execute(text(
            "SELECT 1 FROM pg_database WHERE datname = 'db_escola'"
        )).fetchone()
        if not existe:
            conn.execute(text("CREATE DATABASE db_escola"))
    engine_admin.dispose()

criar_banco()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()