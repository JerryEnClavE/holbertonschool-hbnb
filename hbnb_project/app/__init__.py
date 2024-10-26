from flask import Flask
from .models import init_app as init_models
from .api import register_endpoints

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializa los modelos
    init_models(app)

    # Registra los endpoints de la API
    register_endpoints(app)

    return app
