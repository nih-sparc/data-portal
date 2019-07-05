# shared/views.py

#################
#### imports ####
#################

from app import app
from flask import render_template, Blueprint

################
#### config ####
################

shared_blueprint = Blueprint('shared', __name__, static_folder='./static/dist', template_folder='./static/dist',url_prefix='/shared',static_url_path="")

