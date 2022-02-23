from flask import Flask
from .view import view
from .addInfo import addInfo
from .searchInfo import searchInfo
from flask_sqlalchemy import SQLAlchemy
import os
# Modelo



db = SQLAlchemy()
DB_NAME = "Usuarios.db"


def create_app():

    app = Flask(__name__)
    # Para mantener la sesion del cliente-servidor de forma segura.
    # No es necesario en esta prueba pero es una cuestión de rutina de un desarrollador
    app.config['SECRET_KEY'] = 'Emobotics'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(addInfo, url_prefix='/')
    app.register_blueprint(searchInfo, url_prefix='/')

    from .model import User, Note

    create_database(app)

    return app


def create_database(app):
    if not os.path.exists('WebPage/' + DB_NAME):
        db.create_all(app=app)
        print("Ya está creado")
