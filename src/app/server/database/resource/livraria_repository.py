from server.database.connection.session_factory import session_factory
from server.database.models.Livro import Livro
from typing import Optional


def get_all() -> Optional[list[Livro]]:
    with session_factory() as session:
        livros = [livro.to_json() for livro in session.query(Livro).all()]
        return livros if len(livros) > 0 else None

def get_by_id(id: int) -> Optional[Livro]:
    with session_factory() as session:
        livro = session.query(Livro).get(id)
    return livro

def inserir_livro(livro: Livro) -> None:
    with session_factory() as session:
        try: 
            session.add(livro)
            session.commit()
        except:
            session.rollback()
            raise Exception('Erro ao adicionar item')

def alterar_livro(id: int, livro: Livro) -> None:
    livro_to_update = get_by_id(id)
    
    with session_factory() as session:
        try:
            livro_to_update.nome = livro.nome
            livro_to_update.ano = livro.ano
            livro_to_update.autor = livro.autor
            session.commit()
        except:
            session.rollback()
            raise Exception('Erro ao alterar livro')

def deletar_livro(id):
    livro = get_by_id(id)
    if livro is None: 
        raise Exception('Não foi possivel encontrar o livro')
    
    with session_factory() as session:
        try:
            session.delete(livro)
            session.commit
        except:
            session.rollback()
            raise Exception('Houve um erro ao deletar o livro')