from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date, DateTime, func, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()


class Developer(Base):
    __tablename__ = "developers"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)

    def __repr__(self):
        return f"Developer_id: {self.id} Developer_name: {self.name}"


class Genre(Base):
    __tablename__ = "genres"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)

    def __repr__(self):
        return f"Genre_id: {self.id} Genre_name: {self.name}"


class Platform(Base):
    __tablename__ = "platforms"
    id = Column("id", Integer, primary_key=True)
    console_name = Column("console_name", String, nullable=False)

    def __repr__(self):
        return f"Platform_id: {self.id} Console_name: {self.console_name}"


class Game(Base):
    __tablename__ = "games"
    id = Column("id", Integer, primary_key=True)
    title = Column("title", String, nullable=False)
    release_date = Column("release_date", Date, server_default=func.now(), onupdate=func.now())
    description = Column("description", String)
    gameplay_modes = Column("gameplay_modes", String)
    img_url = Column("img_url", String)

    developer_id = Column("developer_id", Integer, ForeignKey("developers.id", ondelete="CASCADE"), index=True)
    genre_id = Column("genre_id", Integer, ForeignKey("genres.id", ondelete="CASCADE"), index=True)
    platform_id = Column("platform_id", Integer, ForeignKey("platforms.id", ondelete="CASCADE"), index=True)

    def __repr__(self):
        return f"Game_id: {self.id} Title: {self.title} Release_date: {self.release_date}"


class Pricing(Base):
    __tablename__ = "prices"
    game_id = Column("game_id", Integer, ForeignKey("games.id", ondelete="CASCADE"), primary_key=True)
    year = Column("year", Integer, primary_key=True)
    price = Column("price", Float)

    def __repr__(self):
        return f"Game_id: {self.game_id} Year: {self.year} Price: {self.price}"



def create_engine_and_session(database_url):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def seed_data(session):
    # Seed Developers
    developer1 = Developer(name="Developer 1")
    developer2 = Developer(name="Developer 2")
    session.add_all([developer1, developer2])
    session.commit()

    # Seed Genres
    genre1 = Genre(name="Action")
    genre2 = Genre(name="Adventure")
    session.add_all([genre1, genre2])
    session.commit()

    # Seed Platforms
    platform1 = Platform(console_name="PlayStation")
    platform2 = Platform(console_name="Xbox")
    session.add_all([platform1, platform2])
    session.commit()

    # Seed Games
    game1 = Game(
        title="Game 1",
        release_date=datetime(2022, 1, 1),
        description="Description for Game 1",
        gameplay_modes="Single Player",
        img_url="game1.jpg",
        developer_id=developer1.id,
        genre_id=genre1.id,
        platform_id=platform1.id
    )

    game2 = Game(
        title="Game 2",
        release_date=datetime(2022, 2, 1),
        description="Description for Game 2",
        gameplay_modes="Multiplayer",
        img_url="game2.jpg",
        developer_id=developer2.id,
        genre_id=genre2.id,
        platform_id=platform2.id
    )

    session.add_all([game1, game2])
    session.commit()

    # Seed Pricing
    pricing1 = Pricing(game_id=game1.id, year=2022, price=49.99)
    pricing2 = Pricing(game_id=game2.id, year=2022, price=59.99)
    session.add_all([pricing1, pricing2])
    session.commit()
