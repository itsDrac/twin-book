from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Company.query.get(int(id))

class Company(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    number = db.Column(db.Integer(), unique = True)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(60), nullable = False)
