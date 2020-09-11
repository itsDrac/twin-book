from flask import render_template, redirect, url_for
from app import app


@app.route('/')
def home():
    if True :
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/promanag')
def promanag():
    return render_template('proManag.html') 

@app.route('/proadd')
def proadd():
    return render_template('proadd.html')

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
    return redirect(url_for('login'))
