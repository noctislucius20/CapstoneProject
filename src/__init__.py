from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

from flask_migrate import Migrate

DB_NAME = "capstone"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '0d6d55a89139aa5e2b1640f87a1f4abb'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://localhost/{DB_NAME}?user=postgres&password=scipio'
    app.config['JSON_SORT_KEYS'] = False
    db.init_app(app)

    migrate = Migrate(app, db)

    from controllers.User import user

    app.register_blueprint(user, url_prefix='/')

    
    # create_database(app)
    

    return app

# def create_database(app):
#     if not path.exists('src/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')  