from app.models import Company
from app.extinsions import db
from app.company import comp
from app.company.forms import RegisterForm, LoginForm
from flask import render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

@comp.route('/')
def home():
    if not current_user.is_authenticated :
        return redirect(url_for('comp.login'))
    return render_template('dashboard.html')

@comp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated :
        return redirect(url_for('comp.home'))
    form = LoginForm()
    if form.validate_on_submit():
        company = Company.query.filter_by(name=form.name.data).first()
        if company and company.password == form.password.data:
            login_user(company, remember=False)
            return redirect(url_for('comp.home'))
    return render_template('login.html', form=form)


@comp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated :
        return redirect(url_for('comp.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        c = Company(name = form.name.data, number = form.number.data, email = form.email.data, password = form.password.data)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('comp.login'))
    return render_template('register.html', form=form)

@comp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('comp.login'))
