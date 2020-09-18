from app.unit import unit
from app.unit.forms import UnitForm
from app.models import Unit
from app.extinsions import db
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required


@unit.route('/', methods = ['GET','POST'])
@login_required
def home():
    form = UnitForm()
    unites = Unit.query.filter_by(company_id = current_user.id)
    if form.validate_on_submit():
        unit = Unit(name = form.name.data, company_id = current_user.id)
        db.session.add(unit)
        db.session.commit()
        return redirect(url_for('unit.home'))
    return render_template('unit.html', unites=unites, form=form)

@unit.route('/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    form = UnitForm()
    unit = Unit.query.get(id)
    if form.validate_on_submit():
        unit.name = form.name.data
        db.session.commit()
        return redirect(url_for('unit.home'))
    form.name.data = unit.name
    return render_template('unitedit.html', form = form)

@unit.route('/delete/<int:id>', methods = ['GET','POST'])
def delete(id): 
    unit = Unit.query.get(id)
    db.session.delete(unit)
    db.session.commit()
    return redirect(url_for('unit.home'))

