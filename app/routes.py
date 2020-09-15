from flask import render_template, redirect, url_for
from app.extinsions import db
from app.forms import RegisterForm, LoginForm, InventoryForm
from app.models import Company, Inventory
from flask_login import login_user, current_user, logout_user, login_required
from app import create_app
app=create_app()

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

#@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
