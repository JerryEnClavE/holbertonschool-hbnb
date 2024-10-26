from flask import Blueprint
from .users import user_bp
from .places import place_bp
from .reviews import review_bp
from .amenities import amenity_bp

def register_endpoints(app):
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(place_bp, url_prefix='/places')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(amenity_bp, url_prefix='/amenities')
