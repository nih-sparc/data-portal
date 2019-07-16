# sim_core/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint
from logger import logger
from flask import current_app

################
#### config ####
################
 
sim_core_blueprint = Blueprint('sim_core', __name__, static_folder='../shared/static/dist', template_folder='./static/dist', url_prefix='/sim', static_url_path="")

################
#### routes ####
################
 
@sim_core_blueprint.route('/')
def index():
    return render_template('sim.html')