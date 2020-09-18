from flask import Blueprint

pur = Blueprint('pur', __name__, template_folder = 'templates', static_folder='static')

from . import routes

