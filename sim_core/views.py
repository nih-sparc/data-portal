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
 
sim_core_blueprint = Blueprint('sim_core', __name__, template_folder='templates', url_prefix='/sim')

################
#### routes ####
################
 
@sim_core_blueprint.route('/')
def index():
    return render_template('sim_core.html')