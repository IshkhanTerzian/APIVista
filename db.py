from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


def create_engine_and_session(database_url):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
