from ..models.amenity import Amenity
from ..models import db

def create_amenity(description):
    """Crea una nueva amenidad y la guarda en la base de datos."""
    new_amenity = Amenity(description=description)
    db.session.add(new_amenity)
    db.session.commit()
    return new_amenity

def get_amenity(amenity_id):
    """Devuelve una amenidad por su ID."""
    return Amenity.query.get(amenity_id)

def get_all_amenities():
    """Devuelve todas las amenidades."""
    return Amenity.query.all()
