from resource.models.Estoque import Estoque, engine
from resource.models.Livros import Livro, ModelBase


ModelBase.metadata.create_all(bind=engine)
