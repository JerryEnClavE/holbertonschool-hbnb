# app/api/amenity.py
from flask_restx import Namespace, Resource, fields
from flask import request
from app.models.amenity import Amenity  # Adjust the import based on your project structure
from app.repositories.amenity_repository import AmenityRepository  # Assuming you have a repository for Amenity

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'id': fields.String(required=True, description='The amenity unique identifier'),
    'name': fields.String(required=True, description='The name of the amenity'),
})

amenity_repository = AmenityRepository()  # Initialize the amenity repository

@api.route('/')
class AmenityList(Resource):
    @api.doc('create_amenity')
    @api.expect(amenity_model)
    @api.response(201, 'Amenity created successfully')
    def post(self):
        """Create a new amenity"""
        data = request.json
        new_amenity = Amenity(name=data['name'])
        amenity_repository.add(new_amenity)
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201

    @api.doc('list_amenities')
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        amenities = amenity_repository.all()
        return [amenity for amenity in amenities], 200

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.doc('get_amenity')
    @api.response(200, 'Amenity found')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get an amenity by ID"""
        amenity = amenity_repository.get(amenity_id)
        if amenity:
            return {
                'id': amenity.id,
                'name': amenity.name
            }, 200
        return {'message': 'Amenity not found'}, 404

    @api.doc('update_amenity')
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Update an amenity by ID"""
        data = request.json
        amenity = amenity_repository.get(amenity_id)
        if amenity:
            amenity.name = data.get('name', amenity.name)
            amenity_repository.update(amenity)
            return {'id': amenity.id, 'name': amenity.name}, 200
        return {'message': 'Amenity not found'}, 404
