from flask import Flask
from .extinsions import db, migrate, login_manager
from app.company import comp
from app.inventory import inv
from app.unit import unit
from app.product import pro
from app.purchase import pur
from app.vendor import vend

def create_app(config='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(comp)
    app.register_blueprint(inv, url_prefix='/inventory')
    app.register_blueprint(unit, url_prefix='/unit')
    app.register_blueprint(pro, url_prefix='/product')
    app.register_blueprint(pur, url_prefix='/purchase')
    app.register_blueprint(vend, url_prefix='/vendor')

    return app

