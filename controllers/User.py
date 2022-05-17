from flask import Blueprint, request, jsonify, make_response
from nanoid import generate
from werkzeug.security import generate_password_hash, check_password_hash
from models.User import User
from src import db
from functools import wraps

import jwt
import datetime

user = Blueprint('user', __name__)

# decorator as middleware
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return make_response(jsonify({'msg': 'Token is missing!'}), 401)
        
        # decode token
        try:
            output = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            return make_response(jsonify({'msg': 'Token is invalid!'}), 401)
        
        return f(*args, **kwargs)
    
    return decorator

@user.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(id = f'user-{generate(size=16)}', username = data['username'], password = hashed_password, full_name = data['fullName'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "New user created"})

@user.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    logged_in = check_password_hash(user.password, data['password'])
    # check password user
    if not logged_in:
        return jsonify({"message": "Wrong password"}), 401
    
    token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret', algorithm='HS256')
    return make_response(jsonify({'token': token}))

@user.route('/users/<username>', methods=['GET'])
@token_required
def get_one_user(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message" : "User not exist"})
    
    user_data = {}
    user_data['id'] = user.id
    user_data['username'] = user.username
    user_data['fullName'] = user.full_name
    
    return jsonify({'user' : user_data})


    



