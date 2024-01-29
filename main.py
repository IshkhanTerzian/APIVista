import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from db import Developer, Genre, Platform, Game, Pricing, create_engine_and_session, seed_data

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

session = create_engine_and_session(DATABASE_URL)
# db.seed_data(session)


app = Flask(__name__)


@app.route('/')
def home():
    return 'APIVista Home Page'


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
    name = request.args.get('name')
    new_developer = Developer(name=name)
    session.add(new_developer)
    session.commit()
    return jsonify(message="Successfully added the new Developer"), 200


# Update a Developer
@app.route("/api/developer/<int:developer_id>", methods=['PATCH'])
def update_developer(developer_id):
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
    results = session.query(Developer).filter(Developer.id == developer_id)
    developer = results.scalar()

    if not developer:
        return jsonify(error="Developer not found"), 404

    session.delete(developer)
    session.commit()
    return jsonify(message="Successfully Deleted the Developer"), 200
