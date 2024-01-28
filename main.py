from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

database_uri = os.getenv('DATABASE_URI')

if not database_uri:
    raise RuntimeError("DATABASE_URI is not set in the environment variables.")

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db = SQLAlchemy(app)


class Base(DeclarativeBase):
    pass


# =====================
# Start of Genre Model
# =====================
class Genre(db.Model):
    """
    Model representing the Genre table.

    Attributes:
    - id (int): Primary key for the Genre.
    - name (str): Name of the genre.
    """
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)


# ========================
# Start of Developer Model
# ========================
class Developer(db.Model):
    """
    Model representing the Developer table.

    Attributes:
    - id (int): Primary key for the Developer.
    - name (str): Name of the developer (unique).
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)


# =====================
# Start of Game Model
# =====================
class Game(db.Model):
    """
    Model representing the Game table.

    Attributes:
    - id (int): Primary key for the Game.
    - title (str): Title of the game.
    - release_date (date): Release date of the game.
    - genre_id (int): Foreign key referencing Genre table.
    - developer_id (int): Foreign key referencing Developer table.
    - description (text): Description of the game.
    - gameplay_modes (str): Gameplay modes of the game.
    - created_at (datetime): Timestamp of creation.
    - updated_at (datetime): Timestamp of last update.
    - image_url (str): URL for the game's image.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    release_date = db.Column(db.Date)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'))
    description = db.Column(db.Text)
    gameplay_modes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    image_url = db.Column(db.String(255))


# =====================
# Start of Pricing Model
# =====================
class Pricing(db.Model):
    """
    Model representing the Pricing table.

    Attributes:
    - game_id (int): Foreign key referencing Game table.
    - year (int): Year for the pricing information.
    - price (decimal): Price of the game for the year.
    - total_revenue (decimal): Total revenue for the game.
    """
    game_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.DECIMAL(10, 2))
    total_revenue = db.Column(db.DECIMAL(15, 2))
    game = db.relationship('Game', backref='pricing')


# =====================
# Start of Sales Model
# =====================
class Sales(db.Model):
    """
    Model representing the Sales table.

    Attributes:
    - game_id (int): Foreign key referencing Game table.
    - year (int): Year for the sales information.
    - digital_sales (int): Number of digital sales.
    - hard_copy_sales (int): Number of hard copy sales.
    - total_revenue (decimal): Total revenue from sales.
    """
    game_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    digital_sales = db.Column(db.Integer)
    hard_copy_sales = db.Column(db.Integer)
    total_revenue = db.Column(db.DECIMAL(15, 2))
    game = db.relationship('Game', backref='sales')


# =======================
# Start of Platform Model
# =======================
class Platform(db.Model):
    """
    Model representing the Platform table.

    Attributes:
    - id (int): Primary key for the Platform.
    - name (str): Name of the platform (unique).
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


# ==========================
# Start of GamePlatform Model
# ==========================
class GamePlatform(db.Model):
    """
    Model representing the GamePlatform table.

    Attributes:
    - game_id (int): Foreign key referencing Game table.
    - platform_id (int): Foreign key referencing Platform table.
    """
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'), primary_key=True)


# =========================
# Start of GenrePlatform Model
# =========================
class GenrePlatform(db.Model):
    """
    Model representing the GenrePlatform table.

    Attributes:
    - genre_id (int): Foreign key referencing Genre table.
    - platform_id (int): Foreign key referencing Platform table.
    """
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'), primary_key=True)


# ==============================
# Start of DeveloperPlatform Model
# ==============================
class DeveloperPlatform(db.Model):
    """
    Model representing the DeveloperPlatform table.

    Attributes:
    - developer_id (int): Foreign key referencing Developer table.
    - platform_id (int): Foreign key referencing Platform table.
    """
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'), primary_key=True)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'), primary_key=True)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
