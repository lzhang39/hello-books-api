from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import request

from flask import jsonify

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
# APP CONFIG
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
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
