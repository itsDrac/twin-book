from app.extinsions import db
from app.purchase import pur
from app.purchase.forms import PurchaseForm
from app.models import Inventory, Purchase, Unit, QuantityPerPurchase
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

@pur.route('/')
def home():
    purchases = Purchase.query.filter_by(company_id = current_user.id).all()
    return render_template('purchase.html')

@pur.route('/add', methods=['GET','POST'])
def add():
    form = PurchaseForm()
    for field in form.item_quantity:
        field.item_id.choices = [(i.id, i.name) for i in Inventory.query.filter_by(company_id = current_user.id).order_by('name')]
        field.unit_id.choices = [(u.id, u.name) for u in Unit.query.filter_by(company_id = current_user.id).order_by('name')]
    if form.validate_on_submit():
        d = lambda f: f.data       # d = Data and f = field
        purchase = Purchase(party_name = d(form.name), current_date = d(form.current_date), suplier_date = d(form.suplier_date), invoice = d(form.invoice), company_id = current_user.id)
        for item in form.item_quantity.data:
            qpp = QuantityPerPurchase(inventory_id = item['item_id'], unit_id = item['unit_id'], quantity = item['quantity'], price = item['price'])
            db.session.add(qpp)
            purchase.items.append(qpp)
        db.session.add(purchase)
        db.session.commit()
        return redirect(url_for('pur.home'))
    return render_template('purcadd.html', form = form)

@pur.route('/edit/<int:id>')
def edit(id):
    return 'Edit Page'

@pur.route('/delete/<int:id>')
def delete(id):
    return 'Delete page'
