from flask import Blueprint, jsonify, request
from ..services.amenity_service import get_amenity

amenity_bp = Blueprint('amenity', __name__)

@amenity_bp.route('/', methods=['GET'])
def get_amenities():
    # Aquí podrías agregar lógica para obtener todas las amenidades
    return jsonify({'message': 'List of amenities'})

@amenity_bp.route('/<int:amenity_id>', methods=['GET'])
def get_amenity_by_id(amenity_id):
    amenity = get_amenity(amenity_id)
    if amenity:
        return jsonify({'id': amenity.id, 'description': amenity.description}), 200
    else:
        return jsonify({'error': 'Amenity not found'}), 404
