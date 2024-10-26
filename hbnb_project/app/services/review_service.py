from ..models.review import Review
from ..models import db

def create_review(text, user_id, place_id):
    
    new_review = Review(text=text, user_id=user_id, place_id=place_id)
    db.session.add(new_review)
    db.session.commit()
    return new_review

def get_review(review_id):
    
    return Review.query.get(review_id)

def get_all_reviews():
    
    return Review.query.all()
