from typing import List, Optional
from pydantic import BaseModel


class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str

class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True

class EstudanteCreate(BaseModel):
    nome: str
    gmail: str
    perfil: PerfilCreate



class Disciplina(BaseModel):
    id: int
    nome_disciplina: str
    nome_professor: str

    class Config:
        from_attributes = True

class CreateDisciplina(BaseModel):
    nome_disciplina: str
    nome_professor: str



class Matricula(BaseModel):
    id: int
    estudante_id: int
    nome_disciplina: str

    class Config:
        from_attributes = True

class CreateMatricula(BaseModel):
    estudante_id: int
    nome_disciplina: str









class Professor(BaseModel):
    id: int
    nome_professor: str
    nome_disciplina: str

    class Config:
        from_attributes = True

class CreateProfessor(BaseModel):
    nome_professor: str
    nome_disciplina: str
