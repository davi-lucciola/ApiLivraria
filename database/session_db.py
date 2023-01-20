from database.__engine import engine
from sqlalchemy.orm import sessionmaker, Session


def session_factory() -> Session:
    session: Session = sessionmaker(bind=engine)
    return session()