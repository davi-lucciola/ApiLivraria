from database.models.ModelBase import *


class Livro(ModelBase):
    __tablename__ = 'livros'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(80), nullable=False)
    ano: int = Column(Integer, nullable=True)
    autor: str = Column(String(50), nullable=True)
    
    def __repr__(self) -> str:
        return f'<{self.nome} | {self.ano}>'