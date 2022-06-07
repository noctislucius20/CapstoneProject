import json
from src.models.FoodModel import Food as Foodmodel
from src import db
from src.exceptions.InvariantError import InvariantError
import urllib.request
from sqlalchemy import func
import os
from dotenv import load_dotenv

load_dotenv()

class FoodService:
    def add_food(self, food_name, energi, protein, karbohidrat_total, lemak_total):
        self.check_if_food_exist(food_name)
        new_food = Foodmodel(food_name = food_name, energi = energi, protein = protein, karbohidrat_total = karbohidrat_total, lemak_total = lemak_total)

        db.session.add(new_food)
        db.session.commit()

        result = {'food_name': new_food.food_name, 'energi': new_food.energi, 'protein': new_food.protein, 'karbohidrat_total': new_food.karbohidrat_total, 'lemak_total': new_food.lemak_total}
        return result
    
    def get_predicted_food(self, data):
        food = Foodmodel.query.filter(func.lower(Foodmodel.food_name) == func.lower(data['food_name'])).first()

        if not food:
            raise InvariantError(message="Food not exist")
        
        data_to_bytes = json.dumps(data).encode('utf-8')
        host = os.getenv('ML_SERVER_HOST')
        port = os.getenv('ML_SERVER_PORT')
        url = f'http://{host}:{port}/food_recommender/predict'
        req = urllib.request.Request(url, method='GET')
        req.add_header('Content-Type', 'application/json')
        returned_data = urllib.request.urlopen(req, data_to_bytes)
        result = returned_data.read()

        return result

    def check_if_food_exist(self, food_name):
        food = Foodmodel.query.filter(func.lower(Foodmodel.food_name) == func.lower(food_name)).first()

        if food:
            raise InvariantError(message="Food already exists")

    def get_food(self):
        foods = Foodmodel.query.all()
        result = []
        for food in foods:
            data = {}
            data['id'] = food.id
            data['food_name'] = food.food_name
            data['energi'] = food.energi
            data['protein'] = food.protein
            data['karbohidrat_total'] = food.karbohidrat_total
            data['lemak_total'] = food.lemak_total

            result.append(data)

        return result