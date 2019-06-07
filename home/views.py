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
 
home_blueprint = Blueprint('home', __name__, static_folder='./static/dist', template_folder='./static/dist',url_prefix='',static_url_path="")
 
################
#### routes ####
################
 
@home_blueprint.route('/')
def index():
    return render_template('home.html')
