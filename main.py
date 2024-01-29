import os

from flask import Flask, jsonify, request
from models import Developer, Genre, Platform, Game, Pricing
from db import create_engine_and_session
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

session = create_engine_and_session(DATABASE_URL)

app = Flask(__name__)


@app.route('/')
def home():
    return 'APIVista Home Page'


# ============================ DEVELOPERS START =====================================

# Getting all Developers
@app.route('/api/developer')
def get_all_developers():
    """
    Get all developers.

    Returns:
    - JSON: List of developers.
    """
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
    """
    Get a single developer by ID.

    Parameters:
    - developer_id (int): ID of the developer.

    Returns:
    - JSON: Single developer or an error if not found.
    """
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
    new_developer = Developer(name=name)
    session.add(new_developer)
    session.commit()
    return jsonify(message="Successfully added the new Developer"), 200


# Update a Developer
@app.route("/api/developer/<int:developer_id>", methods=['PATCH'])
def update_developer(developer_id):
    """
    Update a developer by ID.

    Parameters:
    - developer_id (int): ID of the developer to update.

    Returns:
    - JSON: Success message or an error if the developer is not found.
    """
    new_name = request.args.get('name')
    results = session.query(Developer).filter(Developer.id == developer_id)
    developer = results.scalar()

    if not developer:
        return jsonify(error="Developer not found"), 404

    developer.name = new_name
    session.commit()
    return jsonify(message="Successfully Updated the Developer"), 200


# Deleting a developer
@app.route('/api/developer/<int:developer_id>', methods=['DELETE'])
def delete_developer(developer_id):
    """
    Delete a developer by ID.

    Parameters:
    - developer_id (int): ID of the developer to delete.

    Returns:
    - JSON: Success message or an error if the developer is not found.
    """
    results = session.query(Developer).filter(Developer.id == developer_id)
    developer = results.scalar()

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
    """
    Get all genres.

    Returns:
    - JSON: List of genres.
    """
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
    """
    Get a single genre by ID.

    Parameters:
    - genre_id (int): ID of the genre.

    Returns:
    - JSON: Single genre or an error if not found.
    """
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
    """
    Add a new genre.

    Returns:
    - JSON: Success message or an error if unsuccessful.
    """
    name = request.args.get('name')
    new_genre = Genre(name=name)
    session.add(new_genre)
    session.commit()
    return jsonify(message="Successfully added the new Genre"), 200


# Update a Genre
@app.route("/api/genre/<int:genre_id>", methods=['PATCH'])
def update_genre(genre_id):
    """
    Update a genre by ID.

    Parameters:
    - genre_id (int): ID of the genre to update.

    Returns:
    - JSON: Success message or an error if the genre is not found.
    """
    new_name = request.args.get('name')
    results = session.query(Genre).filter(Genre.id == genre_id)
    genre = results.scalar()

    if not genre:
        return jsonify(error="Genre not found"), 404

    genre.name = new_name
    session.commit()
    return jsonify(message="Successfully Updated the Genre"), 200


# Deleting a Genre
@app.route('/api/genre/<int:genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    """
    Delete a genre by ID.

    Parameters:
    - genre_id (int): ID of the genre to delete.

    Returns:
    - JSON: Success message or an error if the genre is not found.
    """
    results = session.query(Genre).filter(Genre.id == genre_id)
    genre = results.scalar()

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
    """
    Get all platforms.

    Returns:
    - JSON: List of platforms.
    """
    platforms = []
    results = session.query(Platform).all()
    for platform in results:
        platform_id = platform.id
        name = platform.console_name
        platforms.append({
            "id": platform_id,
            "name": name
        })
    return jsonify(platforms=platforms), 200


# Get a single Platform
@app.route('/api/platform/<int:platform_id>', methods=['GET'])
def get_single_platform(platform_id):
    """
    Get a single platform by ID.

    Parameters:
    - platform_id (int): ID of the genre.

    Returns:
    - JSON: Single platform or an error if not found.
    """
    platform = session.query(Platform).filter(Platform.id == platform_id).scalar()

    if not platform:
        return jsonify(error="Platform not found"), 404

    found_platform = [{
        "id": platform.id,
        "name": platform.console_name
    }]

    return jsonify(platform=found_platform), 200


# Adding a Platform
@app.route('/api/platform', methods=['POST'])
def add_platform():
    """
    Add a new platform.

    Returns:
    - JSON: Success message or an error if unsuccessful.
    """
    name = request.args.get('name')
    new_platform = Platform(console_name=name)
    session.add(new_platform)
    session.commit()
    return jsonify(message="Successfully added the new Platform"), 200


# Update a Platform
@app.route("/api/platform/<int:platform_id>", methods=['PATCH'])
def update_platform(platform_id):
    """
    Update a platform by ID.

    Parameters:
    - platform_id (int): ID of the genre to update.

    Returns:
    - JSON: Success message or an error if the genre is not found.
    """
    new_name = request.args.get('name')
    results = session.query(Platform).filter(Platform.id == platform_id)
    platform = results.scalar()

    if not platform:
        return jsonify(error="Platform not found"), 404

    platform.console_name = new_name
    session.commit()
    return jsonify(message="Successfully Updated the Platform"), 200


# Deleting a Platform
@app.route('/api/platform/<int:platform_id>', methods=['DELETE'])
def delete_platform(platform_id):
    """
    Delete a platform by ID.

    Parameters:
    - platform_id (int): ID of the genre to delete.

    Returns:
    - JSON: Success message or an error if the platform is not found.
    """
    results = session.query(Platform).filter(Platform.id == platform_id)
    platform = results.scalar()

    if not platform:
        return jsonify(error="Platform not found"), 404

    session.delete(platform)
    session.commit()
    return jsonify(message="Successfully Deleted the Platform"), 200

# ============================ PLATFORM END =======================================
