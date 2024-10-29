# app/api/place.py
from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.place import Place  # Adjust the import based on your project structure
from app.repositories.place_repository import PlaceRepository  # Assuming you have a repository for Place
from app.repositories.user_repository import UserRepository  # Assuming you have a repository for User
from app.repositories.amenity_repository import AmenityRepository  # Assuming you have a repository for Amenity

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'id': fields.String(required=True, description='The place unique identifier'),
    'name': fields.String(required=True, description='The name of the place'),
    'owner_id': fields.String(required=True, description='The ID of the owner (User)'),
    'description': fields.String(required=True, description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'amenities': fields.List(fields.String, description='List of amenity IDs associated with the place'),
})

place_repository = PlaceRepository()  # Initialize the place repository
user_repository = UserRepository()  # Initialize the user repository
amenity_repository = AmenityRepository()  # Initialize the amenity repository

@api.route('/')
class PlaceList(Resource):
    @api.doc('create_place')
    @api.expect(place_model)
    @api.response(201, 'Place created successfully')
    @api.response(400, 'Validation error')
    def post(self):
        """Create a new place"""
        data = request.json
        
        # Validate input data
        if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
            return {'message': 'Price must be a positive number'}, 400
        if not isinstance(data['latitude'], (int, float)) or not (-90 <= data['latitude'] <= 90):
            return {'message': 'Latitude must be between -90 and 90'}, 400
        if not isinstance(data['longitude'], (int, float)) or not (-180 <= data['longitude'] <= 180):
            return {'message': 'Longitude must be between -180 and 180'}, 400
        
        # Ensure the owner exists
        if not user_repository.get(data['owner_id']):
            return {'message': 'Owner not found'}, 404

        new_place = Place(
            name=data['name'],
            owner_id=data['owner_id'],
            description=data['description'],
            price=data['price'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            amenities=data.get('amenities', [])
        )
        place_repository.add(new_place)
        return {
            'id': new_place.id,
            'name': new_place.name,
            'owner_id': new_place.owner_id,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'amenities': new_place.amenities
        }, 201

    @api.doc('list_places')
    @api.marshal_list_with(place_model)
    def get(self):
        """List all places"""
        places = place_repository.all()
        return [place for place in places], 200

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.doc('get_place')
    @api.response(200, 'Place found')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get a place by ID"""
        place = place_repository.get(place_id)
        if place:
            return {
                'id': place.id,
                'name': place.name,
                'owner_id': place.owner_id,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'amenities': place.amenities
            }, 200
        return {'message': 'Place not found'}, 404

    @api.doc('update_place')
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Validation error')
    def put(self, place_id):
        """Update a place by ID"""
        data = request.json
        place = place_repository.get(place_id)
        if place:
            # Validate input data
            if 'price' in data:
                if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
                    return {'message': 'Price must be a positive number'}, 400
                place.price = data['price']
            if 'latitude' in data:
                if not isinstance(data['latitude'], (int, float)) or not (-90 <= data['latitude'] <= 90):
                    return {'message': 'Latitude must be between -90 and 90'}, 400
                place.latitude = data['latitude']
            if 'longitude' in data:
                if not isinstance(data['longitude'], (int, float)) or not (-180 <= data['longitude'] <= 180):
                    return {'message': 'Longitude must be between -180 and 180'}, 400
                place.longitude = data['longitude']
            if 'name' in data:
                place.name = data['name']
            if 'description' in data:
                place.description = data['description']
            if 'amenities' in data:
                place.amenities = data['amenities']

            place_repository.update(place)
            return {
                'id': place.id,
                'name': place.name,
                'owner_id': place.owner_id,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'amenities': place.amenities
            }, 200
        
        return {'message': 'Place not found'}, 404
