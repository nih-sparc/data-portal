# dashboard/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint
from logger import logger

################
#### config ####
################
 
dashboard_blueprint = Blueprint('dashboard', __name__, static_folder='./static/dist', template_folder='./static/dist',url_prefix='',static_url_path="")
 
################
#### routes ####
################
 
@dashboard_blueprint.route('/')
def index():
    return render_template('dashboard.html')
