from server.database.models.ModelBase import *


class Livro(ModelBase):
    __tablename__ = 'livros'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(80), nullable=False)
    ano: int = Column(Integer, nullable=True)
    autor: str = Column(String(50), nullable=True)
    
    def __init__(self, nome: str, ano: int, autor: str) -> None:
        self.nome = nome
        self.ano = ano
        self.autor = autor

    def __repr__(self) -> str:
        return f'<{self.nome} | {self.ano}>'

    def to_json(self) -> dict:
        return {'id': self.id, 'nome': self.nome, 'ano': self.ano, 'autor': self.autor}
    
    def __eq__(self, livro) -> bool:
        return (self.id == livro.id and \
                self.ano == livro.ano and \
                self.nome == livro.nome and \
                self.autor == livro.autor)