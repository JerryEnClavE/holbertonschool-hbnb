# resources/user_resource.py
from flask_restx import Resource, Namespace, fields
from flask import request
from app.services.facade import facade


# Definir el namespace para usuarios
api = Namespace('users', description="Operaciones relacionadas con usuarios")

# Definir el modelo para validación de entrada/salida
user_model = api.model('User', {
    'username': fields.String(required=True, description="Nombre de usuario"),
    'email': fields.String(required=True, description="Correo electrónico"),
    # Añade otros campos necesarios para el usuario
})

@api.route('/')
class UserListResource(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Obtener la lista de usuarios"""
        return facade.get_all_users()
    
    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Crear un nuevo usuario"""
        data = request.json
        return facade.create_user(data), 201

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Obtener un usuario por ID"""
        return facade.get_user(user_id)

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Actualizar un usuario por ID"""
        data = request.json
        return facade.update_user(user_id, data)
