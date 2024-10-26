from ..models.place import Place
from ..models import db

def create_place(name, description):
    """Crea un nuevo lugar y lo guarda en la base de datos."""
    new_place = Place(name=name, description=description)
    db.session.add(new_place)
    db.session.commit()
    return new_place

def get_place(place_id):
    """Devuelve un lugar por su ID."""
    return Place.query.get(place_id)

def get_all_places():
    """Devuelve todos los lugares."""
    return Place.query.all()
