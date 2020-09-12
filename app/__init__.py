from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sqlite:///../Database/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Database/database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)


from .routes import *
