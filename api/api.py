# api/api.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint
from logger import logger
from blackfynn import Blackfynn
from config import Config
from flask_marshmallow import Marshmallow
import json

################
#### config ####
################
 
api_blueprint = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')

bf = None
ma = Marshmallow(app)

@app.before_first_request
def connect_to_blackfynn():
    global bf
#    print(Config.BLACKFYNN_API_TOKEN)

#    bf = Blackfynn(
#       api_token=Config.BLACKFYNN_API_TOKEN,
#       api_secret=Config.BLACKFYNN_API_SECRET,
#       env_override=False,
#       host=Config.BLACKFYNN_API_HOST,
#       concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
#    )

################
#### routes ####
################
 
# This is a demo endpoint -- 
@api_blueprint.route('/dat/datasetname')
def dsname():
    ds = bf.get_dataset('N:dataset:941cba6b-a713-4712-bb6f-0c72302ce6ad')
    return json.dumps(ds.name)

    