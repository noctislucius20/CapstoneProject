from src import db
class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(8), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
