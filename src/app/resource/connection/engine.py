from sqlalchemy import create_engine


# engine = create_engine('mysql+mysqlconnector://root@localhost:3306/livraria')
engine = create_engine('sqlite:///resource/database/livraria.db')