from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
# APP CONFIG
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
# DB INITILIZATION
    db.init_app(app)
# MIGRATE INIT...
    migrate.init_app(app, db)

    # IMPORT MODELS
    from app.models.book import Book

    # CREATE THE MODELS ???

    # REGISTERING A BP !!!
    # Again, these lines make it so that our Blueprint is recognized by our Flask app.
    # We need to do this step each time we make a new Blueprint !!!
    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app
