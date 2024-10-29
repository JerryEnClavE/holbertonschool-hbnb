# app/models/place.py
from app.models.base import Base

class Place(Base):
    def __init__(self, name, description, location, user_id):
        super().__init__()
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id  # Link to the owner (User)
        self.amenities = []  # List to hold related amenities
        self.reviews = []  # List to hold related reviews

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        return f"<Place {self.name} at {self.location}>"
