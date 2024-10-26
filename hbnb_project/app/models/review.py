from . import db

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)

    user = db.relationship('User', backref='reviews')
    place = db.relationship('Place', backref='reviews')

    def __repr__(self):
        return f'<Review {self.id}>'
