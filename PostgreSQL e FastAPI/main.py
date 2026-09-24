from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine) # cria as tabelas no postgresSQL caso não existam

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
    '/estudantes/', 
    response_model=schemas.Resposta_Estudante
    )

def create_student( #cria e salva um estudante no banco de dados
    student: schemas.Criar_Estudante,
    db: Session = Depends(get_db)
    ):
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get(
    '/estudantes/',
    response_model= List[schemas.Resposta_Estudante]
    )
def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students

@app.get("/estudantes/{estudante_id}",
        response_model= schemas.Resposta_Estudante
)
def read_student(estudante_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Estudante).filter(
        models.Estudante.id == estudante_id
    ).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return student


@app.post(
    '/matriculas/', 
    response_model=schemas.Restposta_Matricula
)
def create_matriculas( #cria e salva uma matricula no banco de dados
    matricula: schemas.Criar_Maticula,
    db: Session = Depends(get_db)
    ):
    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get(
    '/matriculas/',
    response_model= List[schemas.Restposta_Matricula]
    )
def read_matriculas(db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).all()
    return matriculas