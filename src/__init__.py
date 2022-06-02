from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy_utils.functions import database_exists
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['JSON_SORT_KEYS'] = False

    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        raise Exception("Database does not exist")

    # app initialization
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # import all models for migrations
    from src.models.UserModel import User
    from src.models.FoodModel import Food

    # register blueprints for route
    from src.controllers.UserController import user
    from src.controllers.AuthController import auth
    from src.controllers.FoodController import food
    from src.controllers.ChatController import chat

    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(food, url_prefix='/')
    app.register_blueprint(chat, url_prefix='/bot')


    return app

 
 