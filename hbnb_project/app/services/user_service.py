from ..models.user import User
from ..models import db

def create_user(name, email):
    
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user(user_id):
    
    return User.query.get(user_id)

def get_all_users():
    
    return User.query.all()
