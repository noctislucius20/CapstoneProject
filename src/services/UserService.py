from flask import make_response
from nanoid import generate
from werkzeug.security import generate_password_hash
from src.models.UserModel import User as UserModel
from src import db
from src.exceptions.InvariantError import InvariantError


class UserService:
    def add_user(self, username, password, fullName, gender, date_of_birth, height, weight):
        
        try:
            self.check_user_exists(username)
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = UserModel(id = f'user-{generate(size=16)}', username = username, password = hashed_password, full_name = fullName, gender = gender, date_of_birth = date_of_birth, height = height, weight = weight)
            
            db.session.add(new_user)
            db.session.commit()
        except:
            print('Database error')

        result = {'id': new_user.id, 'username': new_user.username, 'fullName': new_user.full_name, 'gender': new_user.gender, 'date_of_birth': new_user.date_of_birth, 'height': new_user.height, 'weight': new_user.weight}
        return(result)

    def check_user_exists(self, username):
        user = UserModel.query.filter_by(username=username).first()

        if user:
            raise InvariantError(message="User already exists")

    def get_one_user(self, username):
        user = UserModel.query.filter_by(username=username).first()

        if not user:
            raise InvariantError(message="User not exist")
        
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['fullName'] = user.full_name
        user_data['gender'] = user.gender
        user_data['date_of_birth'] = user.date_of_birth
        user_data['height'] = user.height
        user_data['weight'] = user.weight

        return user_data
