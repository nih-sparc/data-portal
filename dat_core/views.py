# dat_core/views.py
 
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
 
dat_core_blueprint = Blueprint('dat_core', __name__, static_folder='./static/dist', template_folder='./static/dist',url_prefix='/browse',static_url_path="")

################
#### routes ####
################


# Need 'v' because <path> after root is interpreted as static asset
@dat_core_blueprint.route('/')
def index():
    return render_template('browse.html')