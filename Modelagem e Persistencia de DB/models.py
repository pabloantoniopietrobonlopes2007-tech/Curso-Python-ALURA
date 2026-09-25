from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    perfil = relationship(
        "Perfil",
        back_populates="estudante",
        uselist=False,
    )
    matriculas = relationship(
        "Matricula",
        back_populates="estudante"
    )

class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    estudante_id = Column(
        Integer,
        ForeignKey("estudantes.id"),
        unique=True
    )
    estudante = relationship(
        "Estudante",
        back_populates='perfil'
    )






class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True, index=True,unique=True)
    nome_disciplina = Column(String, unique=True)
    nome_professor = Column(String)
    matriculas = relationship(
        "Matricula",
        back_populates="disciplina"
    )
    professores = relationship(
        "Professor",
        back_populates="disciplina"
    )



class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(Integer, primary_key=True, unique=True)
    nome_disciplina = Column(
        String,
        ForeignKey("disciplinas.nome_disciplina")
    )
    estudante_id = Column(  
        Integer,
        ForeignKey("estudantes.id")
    )
    disciplina = relationship(
        "Disciplina",
        back_populates="matriculas"
    )
    estudante = relationship(
        "Estudante",
        back_populates="matriculas"
    )



class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer,primary_key=True, unique=True, index=True)
    nome_professor = Column(String)
    nome_disciplina = Column(
        String,
        ForeignKey("disciplinas.nome_disciplina")
    )
    disciplina = relationship(
        "Disciplina",
        back_populates="professores"
    )
