from flask import Blueprint

vend = Blueprint('vend', __name__, template_folder = 'templates', static_folder='static')

from . import routes

