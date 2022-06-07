from src import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(150), unique=True, nullable=False)
    energi = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    karbohidrat_total = db.Column(db.Float, nullable=False)
    lemak_total = db.Column(db.Float, nullable=False)