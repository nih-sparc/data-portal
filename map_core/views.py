# map_core/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint
from logger import logger

################
#### config ####
################
 
map_core_blueprint = Blueprint('map_core', __name__, static_folder='../shared/static/dist', template_folder='./static/dist', url_prefix='/map', static_url_path="")

################
#### routes ####
################
 
@map_core_blueprint.route('/')
def index():
    return render_template('map_core.html')