from ..models.amenity import Amenity
from ..models import db

def create_amenity(description):
    
    new_amenity = Amenity(description=description)
    db.session.add(new_amenity)
    db.session.commit()
    return new_amenity

def get_amenity(amenity_id):
    
    return Amenity.query.get(amenity_id)

def get_all_amenities():
    
    return Amenity.query.all()
