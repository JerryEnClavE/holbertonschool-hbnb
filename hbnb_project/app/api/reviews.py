from flask import Blueprint, jsonify, request
from ..services.review_service import get_review

review_bp = Blueprint('review', __name__)

@review_bp.route('/', methods=['GET'])
def get_reviews():
    # Aquí podrías agregar lógica para obtener todas las reseñas
    return jsonify({'message': 'List of reviews'})

@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review_by_id(review_id):
    review = get_review(review_id)
    if review:
        return jsonify({'id': review.id, 'text': review.text}), 200
    else:
        return jsonify({'error': 'Review not found'}), 404
