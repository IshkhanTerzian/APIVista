import os
from flask import Flask
from dotenv import load_dotenv
from db import Developer, Genre, Platform, Game, Pricing, create_engine_and_session, seed_data


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

session = create_engine_and_session(DATABASE_URL)
#db.seed_data(session)

