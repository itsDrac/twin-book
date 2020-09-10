from flask import render_template
from app import app


@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/register')
def register():
    return render_template('register.html')
