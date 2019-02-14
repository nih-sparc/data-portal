# core/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint
from logger import logger
from blackfynn import Blackfynn
 
bf = None

################
#### config ####
################
 
dat_core_blueprint = Blueprint('dat_core', __name__, template_folder='templates')

@app.before_first_request
def connect_to_blackfynn():
    global bf
    #bf = Blackfynn(
    #    api_token=Config.BLACKFYNN_API_TOKEN,
    #    api_secret=Config.BLACKFYNN_API_SECRET,
    #    env_override=False,
    #    host=Config.BLACKFYNN_API_HOST,
    #    concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
    #)
 
################
#### routes ####
################
 
@dat_core_blueprint.route('/')
def index():
    return render_template('index.html')

@dat_core_blueprint.route('/browse')
def browse():
    return render_template('browse/browse_dat.html')

