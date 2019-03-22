# api/api.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint, request
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
#### GRAPHDB  routes ####
#########################

@api_blueprint.route('/db/model/<model>')
def model(model):
    
    # Provide support for pagination
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    order_by = request.args.get('orderby')
    descending = request.args.get('desc')

    offset = offset if offset != None else 0
    limit = limit if limit != None else 100
    descending = 'DESC' if descending == 'descending' else ''
    
    if order_by != None:
        cmd = 'MATCH (n:{}) RETURN n ORDER BY n.{} {} SKIP {} LIMIT {}'.format(model, order_by, descending, offset, limit)
    else:
        cmd = 'MATCH (n:{}) RETURN n SKIP {} LIMIT {}'.format(model, offset, limit)

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

# TODO: make sure we store nodes for labels so we have more robust way of getting those

@api_blueprint.route('/db/model/<model>/props')
def getLabelProps(model):
    cmd = 'MATCH (n:{}) RETURN n LIMIT 1'.format(model)

    resp = []
    with gp.session() as session:
        result = session.run(cmd) 
        for k in result:
            resp = k['n'].keys()

    # print(resp)
    return json.dumps(resp)

@api_blueprint.route('/db/labels')
def getLabel():
    cmd = 'MATCH (n) RETURN DISTINCT LABELS(n)'
    resp = list()
    with gp.session() as session:
        result = session.run(cmd)  
        for record in result:
            resp.append(record['LABELS(n)'][1])
    
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