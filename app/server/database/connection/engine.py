from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import os


# engine = create_engine('mysql+mysqlconnector://root@localhost:3306/livraria')
engine: Engine = create_engine(r'sqlite:///app\server\database\livraria.db')