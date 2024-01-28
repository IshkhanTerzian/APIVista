from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gaming_database.db'
db = SQLAlchemy(app)


# Define Genre Table
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define Developer Table
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)


# Define the PlayStation Games Table
class PlayStationGame(db.Model):
    ps_game_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    release_date = db.Column(db.Date)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'))
    description = db.Column(db.Text)
    gameplay_modes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    image_url = db.Column(db.String(255))


# Define the Xbox Games Table
class XboxGame(db.Model):
    xbox_game_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    release_date = db.Column(db.Date)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'))
    description = db.Column(db.Text)
    gameplay_modes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    image_url = db.Column(db.String(255))


# Define the PlayStation Pricing Table
class PlayStationPricing(db.Model):
    ps_game_id = db.Column(db.Integer, db.ForeignKey('play_station_game.ps_game_id'), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.DECIMAL(10, 2))
    total_revenue = db.Column(db.DECIMAL(15, 2))
    play_station_game = db.relationship('PlayStationGame', backref='pricing')


# Define the PlayStation Sales Table
class PlayStationSales(db.Model):
    ps_game_id = db.Column(db.Integer, db.ForeignKey('play_station_game.ps_game_id'), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    digital_sales = db.Column(db.Integer)
    hard_copy_sales = db.Column(db.Integer)
    total_revenue = db.Column(db.DECIMAL(15, 2))
    play_station_game = db.relationship('PlayStationGame', backref='sales')


# Define the Xbox Pricing Table
class XboxPricing(db.Model):
    xbox_game_id = db.Column(db.Integer, db.ForeignKey('xbox_game.xbox_game_id'), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.DECIMAL(10, 2))
    total_revenue = db.Column(db.DECIMAL(15, 2))
    xbox_game = db.relationship('XboxGame', backref='pricing')


# Define the Xbox Sales Table
class XboxSales(db.Model):
    xbox_game_id = db.Column(db.Integer, db.ForeignKey('xbox_game.xbox_game_id'), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    digital_sales = db.Column(db.Integer)
    hard_copy_sales = db.Column(db.Integer)
    total_revenue = db.Column(db.DECIMAL(15, 2))
    xbox_game = db.relationship('XboxGame', backref='sales')


# Create the tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)