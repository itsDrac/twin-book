from flask import Blueprint

unit = Blueprint('unit', __name__, template_folder = 'templates')

from . import routes

