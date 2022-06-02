from flask import Blueprint, request, jsonify, make_response
from src.exceptions.ClientError import ClientError
from src.services.UserService import UserService
from src.controllers.AuthController import token_required

user = Blueprint('user', __name__)

@user.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    try:
        new_user = UserService().add_user(username=data.get('username'), password=data.get('password'), fullName=data.get('fullName'), gender=data.get('gender'), date_of_birth=data.get('date_of_birth'), height=data.get('height'), weight=data.get('weight'))

        response = make_response({"status": "success", "message": "New user created", "data": new_user})
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

@user.route('/users/<username>', methods=['GET'])
@token_required
def get_user_by_username(username):
    try:
        user_data = UserService().get_one_user(username)

        response = make_response({"status": "success", "data": user_data})
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        return response

    except ClientError as e:
        response = make_response({"status": "error", "message": e.message})
        response.status_code = 404
        response.headers['Content-Type'] = 'application/json'
        return response

    except:
        #server error 
        response = make_response({"status": "error", "message": "Server fail"})
        response.status_code = 500
        response.headers['Content-Type'] = 'application/json'
        return response
   
