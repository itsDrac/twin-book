from flask import Blueprint

pur = Blueprint('pur', __name__, template_folder = 'templates')

from . import routes

