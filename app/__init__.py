from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)


from .routes import *
