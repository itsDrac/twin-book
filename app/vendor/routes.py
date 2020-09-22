from app.extinsions import db
from app.vendor import vend
from app.models import Product, Inventory
from app.vendor.forms import VendorForm, VendorProductForm
from flask import render_template, redirect, url_for, jsonify
from flask_login import current_user, login_required

@vend.route('/')
def home():
    return render_template('vendor.html')

@vend.route('/add', methods=['GET','POST'])
def add():
    form = VendorForm()
    for field in form.products:
        field.product_id.choices = [(p.id, p.name) for p in Product.query.filter_by(company_id = current_user.id).order_by('name')]
    if form.validate_on_submit():
        return form.data
    return render_template('vendadd.html', form = form)

@vend.route('/add/<id>')
def add_item(id):
    product = Product.query.filter_by(id = id).first()
    
    itemarray = []
    
    for item in product.items:
        itemobj = {}
        itemobj['name'] = Inventory.query.filter_by(id = item.inventory_id).first().name
        itemobj['per_quantity'] = item.quantity

        itemarray.append(itemobj)

    return jsonify({'items': itemarray})
