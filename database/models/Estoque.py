from database.models.ModelBase import *
from sqlalchemy import ForeignKey


class Estoque(ModelBase):
    __tablename__ = 'estoque_livros'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_livro: int = Column(Integer, ForeignKey("livros.id"), nullable=False, unique=True)
    quantidade: int = Column(Integer, nullable=False)
    
    def __repr__(self) -> str:
        return f'<{self.id_livro} | {self.quantidade}>'