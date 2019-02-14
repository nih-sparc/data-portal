# sim_core/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint
from logger import logger

################
#### config ####
################
 
sim_core_blueprint = Blueprint('sim_core', __name__, template_folder='templates')

################
#### routes ####
################
 
@sim_core_blueprint.route('/sim')
def index():
    return render_template('sim_core.html')