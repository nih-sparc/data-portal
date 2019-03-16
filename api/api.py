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
from neo4j import GraphDatabase, basic_auth
import json

################
#### config ####
################
 
api_blueprint = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')

bf = None
gp = None
ma = Marshmallow(app)

@app.before_first_request
def connect_to_blackfynn():
    global bf
    bf = Blackfynn(
       api_token=Config.BLACKFYNN_API_TOKEN,
       api_secret=Config.BLACKFYNN_API_SECRET,
       env_override=False,
       host=Config.BLACKFYNN_API_HOST,
       concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
    )

@app.before_first_request
def connect_to_graphenedb():
    global gp
    graphenedb_url = Config.GRAPHENEDB_BOLT_URL
    graphenedb_user = Config.GRAPHENEDB_BOLT_USER
    graphenedb_pass = Config.GRAPHENEDB_BOLT_PASSWORD
    gp = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))


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
#### GRAPHDB  routes ####
#########################
@api_blueprint.route('/db/model/<model>')
def model(model):
    cmd = 'MATCH (n:{}) RETURN n LIMIT 25'.format(model)

    resp = list()
    with gp.session() as session:
        result = session.run(cmd)    
        for record in result:
            keys = record['n'].keys()
            item = {}
            for key in keys:
                item[key] = record['n'][key]

            resp.append(item)                

    return json.dumps(resp)

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