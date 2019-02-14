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
 
dat_core_blueprint = Blueprint('dat_core', __name__, template_folder='templates')

################
#### routes ####
################
 
@dat_core_blueprint.route('/')
def index():
    return render_template('index.html')

@dat_core_blueprint.route('/browse')
def browse():
    return render_template('browse/browse_dat.html')

