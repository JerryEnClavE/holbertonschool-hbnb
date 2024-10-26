from flask import Blueprint, jsonify, request
from ..services.user_service import get_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    # Aquí podrías agregar lógica para obtener todos los usuarios
    return jsonify({'message': 'List of users'})

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
