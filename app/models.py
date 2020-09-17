from app.extinsions import db, login_manager
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

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

class QuantityPerItem(db.Model):
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    quantity = db.Column(db.Integer, default = 1)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    stock = db.Column(db.Integer, default = 1)
    items = db.relationship('QuantityPerItem', backref='product')

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    party_name = db.Column(db.String(50))
    current_date = db.Column(db.Date)
    suplier_date = db.Column(db.Date)
    invoice = db.Column(db.String(20), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'), primary_key=True)
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

class StockManagment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), primary_key=True)
    quantity = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)



