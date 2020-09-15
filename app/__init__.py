from flask import Flask
from .extinsions import db, migrate, login_manager
from app.inventory import inv 
from app.company import comp

def create_app(config='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    app.register_blueprint(inv, url_prefix='/inventory')
    app.register_blueprint(comp)

    return app

from .routes import *
