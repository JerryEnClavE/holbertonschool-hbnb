from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Cargar la configuración
    app.config.from_object('config.Config')

    # Importar y registrar Blueprints aquí
    # from app.api.users import users_bp
    # app.register_blueprint(users_bp)

    return app

