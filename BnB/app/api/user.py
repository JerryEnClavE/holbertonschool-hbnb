from flask_restx import Namespace, Resource, fields
from flask import request, abort
from app.models.user import User
from app.repositories.user_repository import UserRepository

api = Namespace('users', description='User operations')

# Modelo de respuesta para errores
error_model = api.model('Error', {
    'message': fields.String(required=True, description='Error message')
})

# Modelo de usuario mejorado
user_model = api.model('User', {
    'id': fields.String(readonly=True, description='The user unique identifier'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name'),
})

user_repository = UserRepository()

@api.route('/')
class UserList(Resource):
    @api.doc('create_user')
    @api.expect(user_model)
    @api.response(201, 'User created successfully', user_model)
    @api.response(400, 'Invalid input', error_model)
    def post(self):
        """Create a new user"""
        try:
            data = request.json
            if not data or 'first_name' not in data or 'last_name' not in data:
                return {'message': 'Missing required fields'}, 400
            
            new_user = User(first_name=data['first_name'], last_name=data['last_name'])
            user_repository.add(new_user)
            return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name}, 201
        except Exception as e:
            return {'message': f'Error creating user: {str(e)}'}, 500

    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    @api.response(200, 'Success', [user_model])
    def get(self):
        """List all users"""
        try:
            users = user_repository.all()
            return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name} 
                   for user in users], 200
        except Exception as e:
            return {'message': f'Error fetching users: {str(e)}'}, 500

@api.route('/<string:user_id>')
@api.param('user_id', 'The user identifier')
class UserResource(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_model)
    @api.response(200, 'Success', user_model)
    @api.response(404, 'User not found', error_model)
    def get(self, user_id):
        """Get a user by ID"""
        try:
            user = user_repository.get(user_id)
            if not user:
                api.abort(404, f"User {user_id} not found")
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name
            }, 200
        except Exception as e:
            return {'message': f'Error fetching user: {str(e)}'}, 500

    @api.doc('update_user')
    @api.expect(user_model)
    @api.marshal_with(user_model)
    @api.response(200, 'Success', user_model)
    @api.response(404, 'User not found', error_model)
    @api.response(400, 'Invalid input', error_model)
    def put(self, user_id):
        """Update a user by ID"""
        try:
            data = request.json
            if not data:
                return {'message': 'No input data provided'}, 400

            user = user_repository.get(user_id)
            if not user:
                api.abort(404, f"User {user_id} not found")

            if 'first_name' in data:
                user.first_name = data['first_name']
            if 'last_name' in data:
                user.last_name = data['last_name']

            user_repository.update(user)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name
            }, 200
        except Exception as e:
            return {'message': f'Error updating user: {str(e)}'}, 500

    @api.doc('delete_user')
    @api.response(204, 'User deleted')
    @api.response(404, 'User not found', error_model)
    def delete(self, user_id):
        """Delete a user by ID"""
        try:
            user = user_repository.get(user_id)
            if not user:
                api.abort(404, f"User {user_id} not found")
            
            user_repository.delete(user_id)
            return '', 204
        except Exception as e:
            return {'message': f'Error deleting user: {str(e)}'}, 500
