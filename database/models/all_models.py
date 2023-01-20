from database.models.Estoque import Estoque, engine
from database.models.Livros import Livro, ModelBase


ModelBase.metadata.create_all(bind=engine)
