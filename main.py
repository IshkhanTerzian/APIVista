import os

from flask import Flask, jsonify, request
from models import Developer, Genre, Platform, Game, Pricing, Sales
from db import create_engine_and_session
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
DATABASE_URL = os.getenv('AWS_POSTGRESQL_URL')

session = create_engine_and_session(DATABASE_URL)

app = Flask(__name__)


@app.route('/')
def home():
    return 'APIVista Home Page'


# ============================ DEVELOPERS START =====================================

# Getting all Developers
@app.route('/api/developer')
def get_all_developers():
    developers = []
    results = session.query(Developer).all()
    for developer in results:
        dev_id = developer.id
        name = developer.name
        developers.append({
            "id": dev_id,
            "name": name
        })
    return jsonify(developers=developers), 200


# Get a single Developer
@app.route('/api/developer/<int:developer_id>', methods=['GET'])
def get_single_developer(developer_id):
    developer = session.query(Developer).filter(Developer.id == developer_id).scalar()

    if not developer:
        return jsonify(error="Developer not found"), 404

    found_developer = [{
        "id": developer.id,
        "name": developer.name
    }]

    return jsonify(developer=found_developer), 200


# Adding a Developer
@app.route('/api/developer', methods=['POST'])
def add_developer():
    """
    Add a new developer.

    Returns:
    - JSON: Success message or an error if unsuccessful.
    """
    name = request.args.get('name')

    developer = session.query(Developer).filter(Developer.name == name).scalar()

    if developer:
        return jsonify(error="Developer already exists."), 404

    new_developer = Developer(name=name)
    session.add(new_developer)
    session.commit()
    return jsonify(message="Successfully added the new Developer"), 200


# Update a Developer
@app.route("/api/developer/<int:developer_id>", methods=['PATCH'])
def update_developer(developer_id):
    new_name = request.args.get('name')
    developer = session.query(Developer).filter(Developer.id == developer_id).scalar()

    if not developer:
        return jsonify(error="Developer not found"), 404

    developer.name = new_name
    session.commit()
    return jsonify(message="Successfully Updated the Developer"), 200


# Deleting a developer
@app.route('/api/developer/<int:developer_id>', methods=['DELETE'])
def delete_developer(developer_id):
    developer = session.query(Developer).filter(Developer.id == developer_id).scalar()

    if not developer:
        return jsonify(error="Developer not found"), 404

    session.delete(developer)
    session.commit()
    return jsonify(message="Successfully Deleted the Developer"), 200


# ============================ DEVELOPERS END =====================================


# ============================ GENRES START =====================================

# Getting all Genres
@app.route('/api/genre')
def get_all_genres():
    genres = []
    results = session.query(Genre).all()
    for genre in results:
        genre_id = genre.id
        name = genre.name
        genres.append({
            "id": genre_id,
            "name": name
        })
    return jsonify(genres=genres), 200


# Get a single Genre
@app.route('/api/genre/<int:genre_id>', methods=['GET'])
def get_single_genre(genre_id):
    genre = session.query(Genre).filter(Genre.id == genre_id).scalar()

    if not genre:
        return jsonify(error="Genre not found"), 404

    found_genre = [{
        "id": genre.id,
        "name": genre.name
    }]

    return jsonify(genre=found_genre), 200


# Adding a Genre
@app.route('/api/genre', methods=['POST'])
def add_genre():
    name = request.args.get('name')

    genre = session.query(Genre).filter(Genre.name == name).scalar()

    if genre:
        return jsonify(message="Genre already exists."), 404

    new_genre = Genre(name=name)
    session.add(new_genre)
    session.commit()
    return jsonify(message="Successfully added the new Genre"), 200


# Update a Genre
@app.route("/api/genre/<int:genre_id>", methods=['PATCH'])
def update_genre(genre_id):
    new_name = request.args.get('name')
    genre = session.query(Genre).filter(Genre.id == genre_id).scalar()

    if not genre:
        return jsonify(error="Genre not found"), 404

    genre.name = new_name
    session.commit()
    return jsonify(message="Successfully Updated the Genre"), 200


# Deleting a Genre
@app.route('/api/genre/<int:genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    genre = session.query(Genre).filter(Genre.id == genre_id).scalar()

    if not genre:
        return jsonify(error="Genre not found"), 404

    session.delete(genre)
    session.commit()
    return jsonify(message="Successfully Deleted the Genre"), 200


# ============================ GENRES END =======================================

# ============================ PLATFORM START =======================================

# Getting all Platforms
@app.route('/api/platform')
def get_all_platform():
    platforms = []
    results = session.query(Platform).all()
    for platform in results:
        platforms.append({
            "id": platform.id,
            "name": platform.name
        })
    return jsonify(platforms=platforms), 200


# Get a single Platform
@app.route('/api/platform/<int:platform_id>', methods=['GET'])
def get_single_platform(platform_id):
    platform = session.query(Platform).filter(Platform.id == platform_id).scalar()

    if not platform:
        return jsonify(error="Platform not found"), 404

    found_platform = [{
        "id": platform.id,
        "name": platform.name
    }]

    return jsonify(platform=found_platform), 200


# Adding a Platform
@app.route('/api/platform', methods=['POST'])
def add_platform():
    name = request.args.get('name')

    platform = session.query(Platform).filter(Platform.name == name).scalar()

    if platform:
        return jsonify(message="Platform already exists."), 404

    new_platform = Platform(name=name)
    session.add(new_platform)
    session.commit()
    return jsonify(message="Successfully added the new Platform"), 200


# Update a Platform
@app.route("/api/platform/<int:platform_id>", methods=['PATCH'])
def update_platform(platform_id):
    new_name = request.args.get('name')
    platform = session.query(Platform).filter(Platform.id == platform_id).scalar()

    if not platform:
        return jsonify(error="Platform not found"), 404

    platform.name = new_name
    session.commit()
    return jsonify(message="Successfully Updated the Platform"), 200


# Deleting a Platform
@app.route('/api/platform/<int:platform_id>', methods=['DELETE'])
def delete_platform(platform_id):
    platform = session.query(Platform).filter(Platform.id == platform_id).scalar()

    if not platform:
        return jsonify(error="Platform not found"), 404

    session.delete(platform)
    session.commit()
    return jsonify(message="Successfully Deleted the Platform"), 200


# ============================ PLATFORM END =======================================

# ============================ GAME START =======================================

# Get all Games
@app.route('/api/game')
def get_all_games():
    games = []
    results = session.query(Game).order_by(Game.id).all()

    for game in results:
        developer_name = session.query(Developer.name).filter(Developer.id == game.developer_id).scalar()
        genre = session.query(Genre.name).filter(Genre.id == game.genre_id).scalar()
        platform = session.query(Platform.name).filter(Platform.id == game.platform_id).scalar()

        games.append({
            "id": game.id,
            "title": game.title,
            "release_date": game.release_date,
            "description": game.description,
            "gameplay_modes": game.gameplay_modes,
            "img_url": game.img_url,
            "developer": developer_name,
            "genre": genre,
            "platform_id": platform
        })

    return jsonify(games=games), 200


# Get a single Game
@app.route('/api/game/<int:game_id>', methods=['GET'])
def get_single_game(game_id):
    game = []
    found_game = session.query(Game).filter(Game.id == game_id).scalar()

    if not found_game:
        return jsonify(error="Game not found"), 404

    developer_name = session.query(Developer.name).filter(Developer.id == found_game.id).scalar()
    genre = session.query(Genre.name).filter(Genre.id == found_game.genre_id).scalar()
    platform = session.query(Platform.name).filter(Platform.id == found_game.platform_id).scalar()

    game.append({
        "id": found_game.id,
        "title": found_game.title,
        "release_date": found_game.release_date,
        "description": found_game.description,
        "gameplay_modes": found_game.gameplay_modes,
        "img_url": found_game.img_url,
        "developer": developer_name,
        "genre": genre,
        "platform_id": platform
    })

    return jsonify(game=game), 200


# Add a Game
@app.route('/api/game', methods=['POST'])
def add_game():
    title = request.args.get('title')
    description = request.args.get('description')
    release_date_str = request.args.get('release_date')
    gameplay_modes = request.args.get('gameplay_modes')
    img_url = request.args.get('img_url')
    developer_name = request.args.get('developer')
    genre_name = request.args.get('genre')
    platform_name = request.args.get('platform')

    platform = session.query(Platform).filter(Platform.name == platform_name).scalar()

    if not platform:
        return jsonify(error="Platform does not exist, please add the Platform to the database"), 404

    existing_game = session.query(Game).filter(Game.title == title, Game.platform_id == platform.id).scalar()

    if existing_game:
        return jsonify(error="Game already exists for this platform."), 409

    developer = session.query(Developer).filter(Developer.name == developer_name).scalar()

    if not developer:
        return jsonify(error="Developer does not exist, please add the developer to the database"), 404

    genre = session.query(Genre).filter(Genre.name == genre_name).scalar()

    if not genre:
        return jsonify(error="Genre does not exist, please add the Genre to the database"), 404

    release_date = datetime.strptime(release_date_str, '%B/%d/%Y').date()

    new_game = Game(title=title, description=description, release_date=release_date, gameplay_modes=gameplay_modes,
                    img_url=img_url, developer_id=developer.id, genre_id=genre.id, platform_id=platform.id)

    session.add(new_game)
    session.commit()

    return jsonify(message="Successfully added the Game"), 200


# Update a Game
@app.route('/api/game/<int:game_id>', methods=['PATCH'])
def update_game(game_id):
    game = session.query(Game).filter(Game.id == game_id).scalar()

    if not game:
        return jsonify(error="Game does not exist"), 404

    title = request.args.get('title')
    description = request.args.get('description')
    gameplay_modes = request.args.get('gameplay_modes')
    img_url = request.args.get('img_url')

    game.title = title
    game.description = description
    game.gameplay_modes = gameplay_modes
    game.img_url = img_url

    session.commit()


# Delete a Game
@app.route('/api/game/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = session.query(Game).filter(Game.id == game_id).scalar()

    if not game:
        return jsonify(error="Game does not exist"), 404

    session.delete(game)
    session.commit()
    return jsonify(message="Successfully delete the Game"), 200


# ============================ GAME END =======================================


# ============================ PRICING START =======================================

# Getting all Pricing information
@app.route('/api/pricing')
def get_all_pricing():
    all_prices = []
    results = session.query(Pricing).all()

    for pricing in results:
        game = session.query(Game).filter(Game.id == pricing.game_id).first()

        if game:
            all_prices.append({
                "title": game.title,
                "year": pricing.year,
                "price": pricing.price
            })

    return jsonify(pricings=all_prices), 200


# Get Pricing for a single Game
@app.route('/api/pricing/<int:game_id>', methods=['GET'])
def get_single_game_pricing(game_id):
    year = request.args.get('year')
    pricing = session.query(Pricing).filter_by(game_id=game_id, year=year).first()

    if not pricing:
        return jsonify(error="Pricing information not found for the specified game and year"), 404

    pricing_info = [{
        "game_id": pricing.game_id,
        "year": pricing.year,
        "price": pricing.price
    }]

    return jsonify(pricing=pricing_info), 200


# Add Pricing for a Game
@app.route('/api/pricing/<int:game_id>', methods=['POST'])
def add_game_pricing(game_id):
    price = request.args.get('price')
    year = request.args.get('year')

    existing_pricing = session.query(Pricing).filter_by(game_id=game_id, year=year).first()

    if existing_pricing:
        return jsonify(error="Pricing information already exists for the specified game and year"), 409

    game_exists = session.query(Game).filter(Game.id == game_id).scalar()

    if not game_exists:
        return jsonify(error="Game not found"), 404

    pricing = Pricing(game_id=game_id, year=year, price=price)
    session.add(pricing)
    session.commit()

    return jsonify(message="Successfully added pricing information for the Game"), 200


# Update Pricing for a Game
@app.route('/api/pricing/<int:game_id>', methods=['PATCH'])
def update_game_pricing_or_year(game_id):
    new_price = request.args.get('price')
    new_year = request.args.get('year')

    pricing = session.query(Pricing).filter_by(game_id=game_id, year=new_year).first()

    if not pricing:
        return jsonify(error="Pricing information not found for the specified game and year"), 404

    pricing.price = new_price
    pricing.year = new_year
    session.commit()

    return jsonify(message="Successfully updated pricing information for the Game"), 200


# Delete Pricing for a Game
@app.route('/api/pricing/<int:game_id>', methods=['DELETE'])
def delete_game_pricing(game_id):
    pricing = session.query(Pricing).filter(Pricing.game_id == game_id).scalar()

    if not pricing:
        return jsonify(error="Pricing information not found for the specified game and year"), 404

    session.delete(pricing)
    session.commit()

    return jsonify(message="Successfully deleted pricing information for the Game"), 200


# ============================ PRICING END =======================================


# ============================ SALES START =======================================

# Getting all Sales information
@app.route('/api/sales')
def get_all_sales():
    all_sales = []
    results = session.query(Sales).all()

    for sale in results:
        game = session.query(Game).filter(Game.id == sale.game_id).first()

        if game:
            all_sales.append({
                "id": game.id,
                "title": game.title,
                "year": sale.year,
                "digital_sales": sale.digital_sales,
                "hard_copy_sales": sale.hard_copy_sales
            })

    return jsonify(sales=all_sales), 200


# Get Sales for a single Game
@app.route('/api/sales/<int:game_id>', methods=['GET'])
def get_single_game_sales(game_id):
    year = request.args.get('year')
    sales = session.query(Sales).filter_by(game_id=game_id, year=year).first()

    if not sales:
        return jsonify(error="Sales information not found for the specified game and year"), 404

    game = session.query(Game).filter(Game.id == game_id).scalar()

    sales_info = [{
        "title": game.title,
        "year": sales.year,
        "digital_sales": sales.digital_sales,
        "hard_copy_sales": sales.hard_copy_sales
    }]

    return jsonify(sales=sales_info), 200


# Add Sales for a Game
@app.route('/api/sales/<int:game_id>', methods=['POST'])
def add_game_sales(game_id):
    digital_sales = request.args.get('digital_sales')
    hard_copy_sales = request.args.get('hard_copy_sales')
    year = request.args.get('year')

    existing_sales = session.query(Sales).filter_by(game_id=game_id, year=year).first()

    if existing_sales:
        return jsonify(error="Sales information already exists for the specified game and year"), 409

    game_exists = session.query(Game).filter(Game.id == game_id).scalar()

    if not game_exists:
        return jsonify(error="Game not found"), 404

    sales = Sales(game_id=game_id, year=year, digital_sales=digital_sales, hard_copy_sales=hard_copy_sales)
    session.add(sales)
    session.commit()

    return jsonify(message="Successfully added sales information for the Game"), 200


# Update Sales for a Game
@app.route('/api/sales/<int:game_id>', methods=['PATCH'])
def update_game_sales_or_year(game_id):
    new_digital_sales = request.args.get('digital_sales')
    new_hard_copy_sales = request.args.get('hard_copy_sales')
    new_year = request.args.get('year')

    sales = session.query(Sales).filter(Sales.game_id == game_id).first()

    if not sales:
        return jsonify(error="Sales information not found for the specified game and year"), 404

    sales.digital_sales = new_digital_sales
    sales.hard_copy_sales = new_hard_copy_sales
    sales.year = new_year
    session.commit()

    return jsonify(message="Successfully updated sales information for the Game"), 200


# Delete Sales for a Game at a specific Year
@app.route('/api/sales/<int:game_id>', methods=['DELETE'])
def delete_game_sales(game_id):
    year = request.args.get('year')
    sales = session.query(Sales).filter(Sales.game_id == game_id, Sales.year == year).first()

    if not sales:
        return jsonify(error="Sales information not found for the specified game and year"), 404

    session.delete(sales)
    session.commit()

    return jsonify(message="Successfully deleted sales information for the Game"), 200


# ============================ SALES END =======================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
