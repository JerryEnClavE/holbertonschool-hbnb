import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:your_password@localhost/HBnB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva la modificación de seguimiento para optimización


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:your_password@localhost/HBnB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el rastreo de modificaciones para evitar warnings.

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
