from . import db

class Amenity(db.Model):
    __tablename__ = 'amenities'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Amenity {self.description}>'
