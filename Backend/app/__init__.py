# app/__init__.py
from flask import Flask
from .extensions import db, migrate, login_manager, cors
from .models import socio,asamblea,deuda
from .resources import init_resources

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    # Inicializa extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cors.init_app(app)

    init_resources(app)
    return app