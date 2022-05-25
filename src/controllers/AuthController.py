from functools import wraps
from flask import Blueprint, jsonify, make_response, request
from werkzeug.security import check_password_hash

import jwt
import datetime

from src.models.UserModel import User as UserModel

auth = Blueprint('auth', __name__)

# decorator as middleware
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization').replace('Bearer ', '')
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
    
    token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret', algorithm='HS256')
    return make_response(jsonify({'token': token}))