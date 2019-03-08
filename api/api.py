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
    print(Config.BLACKFYNN_API_TOKEN)

    bf = Blackfynn(
       api_token=Config.BLACKFYNN_API_TOKEN,
       api_secret=Config.BLACKFYNN_API_SECRET,
       env_override=False,
       host=Config.BLACKFYNN_API_HOST,
       concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
    )

#########################
#### Classes ############
#########################

# class PublishedDataset(Model):
#     name = Column(String)
#     password = Column(String)
#     date_created = Column(DateTime, auto_now_add=True)

# class PublishedDatasetSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ('name', 'date_created', '_links')
#     # Smart hyperlinking
#     _links = ma.Hyperlinks({
#         'self': ma.URLFor('user_detail', id='<id>'),
#         'collection': ma.URLFor('users')
#     })

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

#########################
#### DAT-CORE routes ####
#########################

# Returns a list of public datasets from 
@api_blueprint.route('/datasets')
def discover():
    resp = bf._api._get('/consortiums/1/datasets')
    return json.dumps(resp)

#########################
#### MAP-CORE routes ####
#########################


#########################
#### SIM-CORE routes ####
#########################