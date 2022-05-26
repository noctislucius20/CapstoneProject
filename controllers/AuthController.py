from functools import wraps
from flask import Blueprint, jsonify, make_response, request
from werkzeug.security import check_password_hash

import jwt
import datetime

from models.UserModel import User as UserModel, age

auth = Blueprint('auth', __name__)

# decorator as middleware
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return make_response(jsonify({'status': 'error', 'message': 'Token is missing!'}), 401)
        
        # decode token
        try:
            output = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            return make_response(jsonify({'status': 'error', 'message': 'Token is invalid!'}), 401)
        
        return f(*args, **kwargs)
    
    return decorator

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = UserModel.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    logged_in = check_password_hash(user.password, data['password'])
    # check password user
    if not logged_in:
        return jsonify({"message": "Wrong password"}), 401
    
    user_data = {}
    user_data['id'] = user.id
    user_data['username'] = user.username
    user_data['fullName'] = user.full_name
    user_data['gender'] = user.gender
    user_data['date_of_birth'] = user.date_of_birth
    user_data['height'] = user.height
    user_data['weight'] = user.weight
    
    # Count age of user
    user_data['age'] = age(user.date_of_birth)
        
    token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret', algorithm='HS256')
    return make_response(jsonify({'status': 'OK', 'data': user_data, 'token': token}), 200)