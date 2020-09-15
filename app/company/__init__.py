from flask import Blueprint

comp = Blueprint('comp', __name__, template_folder = 'templates')

from . import routes

