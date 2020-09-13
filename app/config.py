import os

SECRET_KEY = '1b49b02d90b26cddba45d123458e690a'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////'+ os.path.abspath(os.getcwd()) + '/Database/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
