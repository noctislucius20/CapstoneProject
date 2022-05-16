from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "capstone.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '0d6d55a89139aa5e2b1640f87a1f4abb'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .user import user

    app.register_blueprint(user, url_prefix='/')

    create_database(app)

    return app

def create_database(app):
    if not path.exists('src/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')  