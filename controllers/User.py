from flask import Blueprint, request, jsonify, make_response
from nanoid import generate
from werkzeug.security import generate_password_hash, check_password_hash
from controllers.login import token_required
from models.User import User
from src import db

user = Blueprint('user', __name__)

@user.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(id = f'user-{generate(size=16)}', username = data['username'], password = hashed_password, full_name = data['fullName'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "New user created"})

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


    



