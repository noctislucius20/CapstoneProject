from nanoid import generate
from werkzeug.security import generate_password_hash
from models.UserModel import User as UserModel
from src import db
from exceptions.InvariantError import InvariantError


class UserService:
    def add_user(self, username, password, fullName):
        self.check_user_exists(username)
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = UserModel(id = f'user-{generate(size=16)}', username = username, password = hashed_password, full_name = fullName)
        
        db.session.add(new_user)
        db.session.commit()

        result = {'id': new_user.id, 'username': new_user.username, 'fullName': new_user.full_name}
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

        return user_data
