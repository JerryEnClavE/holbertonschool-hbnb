# app/models/base.py
from datetime import datetime
import uuid

class Base:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

# app/models/user.py
from .base import Base

class User(Base):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

# app/models/place.py
from .base import Base

class Place(Base):
    def __init__(self, name, description, location, user_id):
        super().__init__()
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        return f"<Place {self.name} at {self.location}>"

# app/models/review.py
from .base import Base

class Review(Base):
    def __init__(self, content, rating, user_id, place_id):
        super().__init__()
        self.content = content
        self.rating = self.validate_rating(rating)
        self.user_id = user_id
        self.place_id = place_id

    @staticmethod
    def validate_rating(rating):
        if 1 <= rating <= 5:
            return rating
        raise ValueError("Rating must be between 1 and 5")

    def __repr__(self):
        return f"<Review by User {self.user_id} for Place {self.place_id}>"

# app/models/amenity.py
from .base import Base

class Amenity(Base):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"<Amenity {self.name}>"
