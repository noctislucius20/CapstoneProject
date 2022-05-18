from sqlalchemy import true
from src import db

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(30), unique=true, nullable=False)
    password = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.String(100), nullable=False) 

