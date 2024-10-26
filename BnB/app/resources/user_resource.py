# app/resources/user_resource.py
from flask_restx import Resource, Namespace
from app.models.user import User

api = Namespace('users', description='User operations')

@api.route('/')
class UserList(Resource):
    def get(self):
        # Logic to retrieve all users
        pass

    def post(self):
        # Logic to create a new user
        pass

@api.route('/<int:user_id>')
class UserDetail(Resource):
    def get(self, user_id):
        # Logic to retrieve a user by ID
        pass

    def put(self, user_id):
        # Logic to update a user
        pass

    def delete(self, user_id):
        # Logic to delete a user
        pass
