from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy_utils.functions import database_exists
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['JSON_SORT_KEYS'] = False

    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        raise Exception("Database does not exist")

    db.init_app(app)
    migrate.init_app(app, db)
    
    # import all models for migrations
    from src.models.UserModel import User
    from src.models.FoodModel import Food

    # register blueprints for route
    from src.controllers.UserController import user
    from src.controllers.AuthController import auth
    from src.controllers.FoodController import food

    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(food, url_prefix='/')


    return app

 
 