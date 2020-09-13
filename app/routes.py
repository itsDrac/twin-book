from flask import render_template, redirect, url_for
from app import app, db
from app.forms import RegisterForm, LoginForm
from app.models import Company
from flask_login import login_user, current_user, logout_user

@app.route('/')
def home():
    if not current_user.is_authenticated :
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        company = Company.query.filter_by(name=form.name.data).first()
        if company and company.password == form.password.data:
            login_user(company, remember=False)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        c = Company(name = form.name.data, number = form.number.data, email = form.email.data, password = form.password.data)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/promanag')
def promanag():
    return render_template('proManag.html') 

@app.route('/proadd')
def proadd():
    return render_template('proAdd.html')

@app.route('/vendmanag')
def vendmanag():
    return render_template('vendManag.html')

@app.route('/vendadd')
def vendadd():
    return render_template('vendAdd.html')

@app.route('/vendrec')
def vendrec():
    return render_template('vendRec.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
