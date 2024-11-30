from flask_restx import Api
from part2.hbnb.app.api.v1.amenities import api as amenities_ns

api = Api(
    title='HBNB API',
    version='1.0',
    description='A simple API for HBNB',
    doc='/doc'
)

api.add_namespace(amenities_ns, path='/amenities')