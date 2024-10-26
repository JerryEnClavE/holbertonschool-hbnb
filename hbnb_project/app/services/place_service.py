from ..models.place import Place
from ..models import db

def create_place(name, description):
    
    new_place = Place(name=name, description=description)
    db.session.add(new_place)
    db.session.commit()
    return new_place

def get_place(place_id):
    
    return Place.query.get(place_id)

def get_all_places():
    
    return Place.query.all()
