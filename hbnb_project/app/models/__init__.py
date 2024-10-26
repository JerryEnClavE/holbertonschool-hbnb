from flask_sqlalchemy import SQLAlchemy

# Inicializar la base de datos
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
