from sqlalchemy import ForeignKey, Column, String, func, Integer, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Developer(Base):
    """Model for Developers table."""
    __tablename__ = "developers"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False, unique=True)

    def __repr__(self):
        return f"Developer_id: {self.id} Developer_name: {self.name}"


class Genre(Base):
    """Model for Genres table."""
    __tablename__ = "genres"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False, unique=True)

    def __repr__(self):
        return f"Genre_id: {self.id} Genre_name: {self.name}"


class Platform(Base):
    """Model for Platforms table."""
    __tablename__ = "platforms"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False, unique=True)

    def __repr__(self):
        return f"Platform_id: {self.id} name: {self.name}"


class Game(Base):
    """Model for Games table."""
    __tablename__ = "games"
    id = Column("id", Integer, primary_key=True)
    title = Column("title", String, nullable=False)
    release_date = Column("release_date", Date, server_default=func.now(), onupdate=func.now(), nullable=False)
    description = Column("description", String, nullable=False)
    gameplay_modes = Column("gameplay_modes", String, nullable=False)
    img_url = Column("img_url", String)

    developer_id = Column("developer_id", Integer, ForeignKey("developers.id", ondelete="CASCADE"), index=True, nullable=False)
    genre_id = Column("genre_id", Integer, ForeignKey("genres.id", ondelete="CASCADE"), index=True, nullable=False)
    platform_id = Column("platform_id", Integer, ForeignKey("platforms.id", ondelete="CASCADE"), index=True, nullable=False)

    def __repr__(self):
        return f"Game_id: {self.id} Title: {self.title} Release_date: {self.release_date}"


class Pricing(Base):
    """Model for Prices table."""
    __tablename__ = "prices"
    game_id = Column("game_id", Integer, ForeignKey("games.id", ondelete="CASCADE"), primary_key=True)
    year = Column("year", Integer, primary_key=True)
    price = Column("price", Float)

    def __repr__(self):
        return f"Game_id: {self.game_id} Year: {self.year} Price: {self.price}"
