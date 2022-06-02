from flask import Blueprint, request, jsonify, make_response
from src.exceptions.ClientError import ClientError
from src.services.FoodService import FoodService
from src.controllers.AuthController import token_required
import json
import urllib

food = Blueprint('food', __name__)

@food.route('/food', methods=['POST'])
@token_required
def post_food():
    data = request.get_json()
    
    try:
        new_food = FoodService().add_food(food_name=data.get('food_name'), energi=data.get('energi'), protein=data.get('protein'), karbohidrat_total=data.get('karbohidrat_total'), lemak_total=data.get('lemak_total'))

        response = make_response({"status": "success", "message": "New food added", "data": new_food})
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 201
        return response

    except ClientError as e:
        response = make_response({"status": "error", "message": e.message})
        response.status_code = e.statusCode
        response.headers['Content-Type'] = 'application/json'
        return response

    except:
        #server error 
        response = make_response({"status": "error", "message": "Server fail"})
        response.status_code = 500
        response.headers['Content-Type'] = 'application/json'
        return response

@food.route('/food', methods=['GET'])
def get_all_food():
    data = FoodService().get_food()

    response = make_response({"status": "success", "data": data})
    response.headers['Content-Type'] = 'application/json'
    return response
    

@food.route('/food/predict', methods=['POST'])
@token_required
def get_food():
    data = request.get_json()
    try:
    
        result = FoodService().get_predicted_food(data)
        
        response = make_response({"status": "success", "data": json.loads(result)})
        response.headers['Content-Type'] = 'application/json'
        return response
    
    except ClientError as e:
        response = make_response({"status": "error", "message": e.message})
        response.status_code = e.statusCode
        response.headers['Content-Type'] = 'application/json'
        return response

    except urllib.error.HTTPError as e:
        response = make_response({"status": "error", "message": e.reason})
        response.status_code = e.code
        response.headers['Content-Type'] = 'application/json'
        return response

 
