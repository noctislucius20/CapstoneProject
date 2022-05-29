from src.models.FoodModel import Food as Foodmodel
from src import db

class FoodService:
    def add_food(self, food_name, energi, protein, karbohidrat_total, lemak_total):
        new_food = Foodmodel(food_name = food_name, energi = energi, protein = protein, karbohidrat_total = karbohidrat_total, lemak_total = lemak_total)

        db.session.add(new_food)
        db.session.commit()

        result = {'food_name': new_food.food_name, 'energi': new_food.energi, 'protein': new_food.protein, 'karbohidrat_total': new_food.karbohidrat_total, 'lemak_total': new_food.lemak_total}
        return result