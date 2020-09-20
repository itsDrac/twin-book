from app.extinsions import db
from app.product import pro
from app.product.forms import ProductForm, ItemQuantityForm
from app.models import Inventory, Product, QuantityPerItem
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from collections import namedtuple

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
    for field in form.item_quantity:
        print(type(field.item_id))
        field.item_id.choices = [(i.id, i.name) for i in Inventory.query.filter_by(company_id = current_user.id).order_by('name')]
        field.quantity.default = 10
    if form.validate_on_submit():
        return form.data
    form.name.data , form.stock.data = product.name, product.stock
    x = lambda id : (id, Inventory.query.get(id).name)
    #form.item_quantity.item_id.data = [i.inventory_id for i in product.items]
    #form.item_quantity.append_entry = [{'item_id': i.inventory_id, 'quantity': i.quantity} for i in product.items]
    data = []
    for item in product.items:
        #data = [({'item_id': [item.inventory_id], 'quantity': [item.quantity]})]
        group = namedtuple('Group', ['item_id', 'quantity'])
        g = group(item.inventory_id, item.quantity)
        data += g
        print(data)
        form.item_quantity(data = [{'item_id': item.inventory_id, 'quantity': item.quantity}])
        print(type(form.item_quantity))
        print(form.item_quantity.entries[0].item_id.data)
        form.item_quantity(data=data)
    '''
    for item in product.items:
        iq = form.item_quantity()
        print(type(iq))
        iq.item_id.default = item.inventory_id
        print(type(iq.item_id))
        iq.quantity.default = item.quantity
        print(type(iq.quantity))

        form.item_quantity.append_entry(iq)
    '''
    return render_template('proedit.html', form=form)

@pro.route('/delete/<int:id>')
def delete(id):
    qpi = QuantityPerItem.query.filter_by(product_id = id).all()
    for q in qpi:
        db.session.delete(q)
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('pro.home'))
