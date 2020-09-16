from app.inventory import inv
from app.inventory.forms import InventoryForm
from app.models import Inventory
from app.extinsions import db
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required


@inv.route('/', methods = ['GET','POST'])
def home():
    form = InventoryForm()
    items = Inventory.query.filter_by(company_id = current_user.id)
    if form.validate_on_submit():
        item = Inventory(name = form.name.data, company_id = current_user.id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('inventory'))
    return render_template('inventory.html',items=items, form=form)

@inv.route('/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    form = InventoryForm()
    item = Inventory.query.get(id)
    if form.validate_on_submit():
        item.name = form.name.data
        db.session.commit()
    form.name.data = item.name
    return render_template('edit.html', form = form)

@inv.route('/delete/<int:id>', methods = ['GET','POST'])
def delete(id): 
    item = Inventory.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('inv.home'))
