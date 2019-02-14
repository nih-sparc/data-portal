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
 
dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates')
 
################
#### routes ####
################
 
@dashboard_blueprint.route('/')
def index():
    return render_template('index.html')
