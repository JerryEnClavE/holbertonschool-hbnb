from ..models.review import Review
from ..models import db

def create_review(text, user_id, place_id):
    """Crea una nueva reseña y la guarda en la base de datos."""
    new_review = Review(text=text, user_id=user_id, place_id=place_id)
    db.session.add(new_review)
    db.session.commit()
    return new_review

def get_review(review_id):
    """Devuelve una reseña por su ID."""
    return Review.query.get(review_id)

def get_all_reviews():
    """Devuelve todas las reseñas."""
    return Review.query.all()
