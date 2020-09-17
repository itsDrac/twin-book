from app.extinsions import db
from app.product import pro
from app.product.forms import ProductForm
from app.models import Inventory, Product, QuantityPerItem
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

@pro.route('/')
def home():
    products = Product.query.filter_by(company_id = current_user.id).all()
    return render_template('proManag.html', products=products)

@pro.route('/addpro', methods=['GET','POST'])
def add():
    form = ProductForm()
    for field in form.item_quantity:
        field.item_id.choices = [(i.id, i.name) for i in Inventory.query.filter_by(company_id = current_user.id).order_by('name')]
    if form.validate_on_submit():
        product = Product(name = form.name.data, company_id = current_user.id, stock = form.stock.data)        
        for item in form.item_quantity.data:
            qpi = QuantityPerItem(inventory_id = item['item_id'], quantity = item['quantity'])
            db.session.add(qpi)
            product.items.append(qpi)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('pro.home'))
    return render_template('proAdd.html', form=form)

@pro.route('/edit/<int:id>')
def edit(id):
    form = ProductForm()
    product = Product.query.get(id)
    if form.validate_on_submit():
        return form.data
    form.name.data , form.stock.data = product.name, product.stock
    items = product.items
    form.item_quantity.quantity = [i.quantity for i in items]
    return render_template('proedit.html', form=form, items=items)

@pro.route('/delete/<int:id>')
def delete(id):
    qpi = QuantityPerItem.query.filter_by(product_id = id).all()
    for q in qpi:
        db.session.delete(q)
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('pro.home'))
