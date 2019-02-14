# core/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint
from logger import logger

################
#### config ####
################
 
dat_core_blueprint = Blueprint('dat_core', __name__, template_folder='templates', url_prefix='/browse')

################
#### routes ####
################

@dat_core_blueprint.route('/')
def browse():
    return render_template('browse/browse_dat.html')


