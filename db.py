from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


def create_engine_and_session(database_url):
    """
     This function creates an SQLAlchemy engine using the provided database URL,
    initializes the tables defined in the models, and returns a sessionmaker
    instance to create sessions connected to the engine.
    :param database_url: The URL of the database.
    :return: An instance of the SQLAlchemy Session.
    """
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
