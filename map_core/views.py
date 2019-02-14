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
 
map_core_blueprint = Blueprint('map_core', __name__, template_folder='templates', url_prefix='/map')

################
#### routes ####
################
 
@map_core_blueprint.route('/')
def index():
    return render_template('map_core.html')