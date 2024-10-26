from flask import Blueprint, jsonify, request
from ..services.place_service import get_place

place_bp = Blueprint('place', __name__)

@place_bp.route('/', methods=['GET'])
def get_places():
    # Aquí podrías agregar lógica para obtener todos los lugares
    return jsonify({'message': 'List of places'})

@place_bp.route('/<int:place_id>', methods=['GET'])
def get_place_by_id(place_id):
    place = get_place(place_id)
    if place:
        return jsonify({'id': place.id, 'name': place.name}), 200
    else:
        return jsonify({'error': 'Place not found'}), 404
