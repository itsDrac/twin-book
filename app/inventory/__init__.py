from flask import Blueprint

inv = Blueprint('inv', __name__, template_folder = 'templates')

from . import routes
