from database.__engine import engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


ModelBase = declarative_base(bind=engine)