from pydantic import BaseModel

class Estudante_Base(BaseModel):
    nome: str
    idade: int

class Criar_Estudante(Estudante_Base):
    pass

class Resposta_Estudante(Estudante_Base):
    id: int
    class Config:
        from_attributes = True

class Maricula_Base(BaseModel):
    estudante_id: int
    nome_disciplina: str

class Criar_Maticula(Maricula_Base):
    pass

class Restposta_Matricula(Maricula_Base):
    id: int
    class Config:
        from_attibutes = True