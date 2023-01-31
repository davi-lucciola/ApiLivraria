from resource.models.Livro import Livro, ModelBase, engine


ModelBase.metadata.create_all(bind=engine)
