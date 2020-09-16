from flask import Blueprint

pro = Blueprint('pro', __name__, template_folder = 'templates', static_folder='static')

from . import routes

