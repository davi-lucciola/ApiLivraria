from resource.connection.session_db import session_factory
from resource.models.Livro import Livro
from typing import Optional


def inserir_livro(livro: Livro):
    with session_factory() as session:
        try: 
            session.add(livro)
            session.commit()
        except:
            session.rollback()
            raise Exception("Erro ao adicionar item")

def get_by_id(id: int) -> Livro:
    with session_factory() as session:
        livro = session.query(Livro).get(id)
    
    return livro

def get_all() -> Optional[list[Livro]]:
    with session_factory() as session:
        livros = [livro.to_json() for livro in session.query(Livro).all()]
        return livros if len(livros) > 0 else None