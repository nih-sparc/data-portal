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
import urllib

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

    # bf = Blackfynn(
    #    api_token=Config.BLACKFYNN_API_TOKEN,
    #    api_secret=Config.BLACKFYNN_API_SECRET,
    #    env_override=False,
    #    host=Config.BLACKFYNN_API_HOST,
    #    concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
    # )

@app.before_first_request
def connect_to_graphenedb():
    global gp
    # graphenedb_url = Config.GRAPHENEDB_BOLT_URL
    # graphenedb_user = Config.GRAPHENEDB_BOLT_USER
    # graphenedb_pass = Config.GRAPHENEDB_BOLT_PASSWORD
    # gp = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))

#########################
#### GRAPHDB  routes ####
#########################
@api_blueprint.route('/db/graph/properties')
def graph_props():
    cmd = 'MATCH (n:GraphModel)-[*1]-(m:GraphModelProp) RETURN n.name, m.name'
    with gp.session() as session:
        result = session.run(cmd)
        items = []
        for record in result:
            items.append({'model': record['n.name'], 'prop': record['m.name']})

    return json.dumps(items)

@api_blueprint.route('/db/model/<model>')
def model(model):
    
    # Get Request parameters and stage Cypher cmd
    args = request.args

    # Provide support for pagination
    offset = args.get('offset')
    limit = args.get('limit')
    order_by = args.get('orderby')
    descending = args.get('desc')
    hops = args.get('hops')

    offset = offset if offset != None else 0
    limit = limit if limit != None else 100
    hops = hops if hops != None else 1
    descending = 'DESC' if descending == 'descending' else ''
    
    filters = json.loads(urllib.unquote(args.get('filters')).decode('utf8'))
    print(filters)

    if filters:
        cmd = ''
        # Add MATCH statements 
        for idx, f in enumerate(filters):
            propComponents = f['m'].split(':')
            propModel = propComponents[0]
            propProperty = propComponents[1]
            if model != propModel:
                cmd += 'MATCH (n:{})-[*0..{}]-(m{}:{}) '.format(model,hops,idx,propModel)
            elif idx == 0:
                cmd += 'MATCH (n:{}) '.format(model)

        # Add WHERE statements
        for idx, f in enumerate(filters):
            if idx > 0:
                cmd += 'AND '
            else :
                cmd += 'WHERE '

            propComponents = f['m'].split(':')
            propModel = propComponents[0]
            propProperty = propComponents[1]
            if model == propModel:
                cmd += 'n.{} {} {} '.format(propProperty, f['o'], f['v'])
            else:
                cmd += 'm{}.{} {} {} '.format(idx, propProperty, f['o'], f['v'])

        # Add RETURN
        cmd += 'RETURN distinct n'

        # Set Order Info
        if order_by:
            cmd += ' ORDER BY n.{} {}'.format(order_by, descending)

        # Set Pagination Info
        cmd += ' SKIP {} LIMIT {}'.format( offset, limit)

    else:
        if order_by:
            cmd = 'MATCH (n:{}) RETURN n ORDER BY n.{} {} SKIP {} LIMIT {}'.format(model, order_by, descending, offset, limit)
        else:
            cmd = 'MATCH (n:{}) RETURN n SKIP {} LIMIT {}'.format(model, offset, limit)
        
    print('requesting: {}'.format(cmd))    
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

@api_blueprint.route('/db/model/<model>/props')
def getLabelProps(model):
    cmd = 'MATCH (a:{}) UNWIND keys(a) AS key RETURN collect(distinct key)'.format(model)

    # cmd = 'MATCH (n:{}) RETURN n LIMIT 1'.format(model)
    print(cmd)

    resp = []
    with gp.session() as session:
        result = session.run(cmd) 
        # print(result)
        for k in result:
            col = k['collect(distinct key)']
            for item in col:
                resp.append(item)

    return json.dumps(resp)

@api_blueprint.route('/db/labels')
def getLabel():
    cmd = 'MATCH (n:Node) RETURN DISTINCT LABELS(n)'
    resp = list()
    with gp.session() as session:
        result = session.run(cmd)  
        for record in result:
            resp.append(record['LABELS(n)'][1])
    
    return json.dumps(resp)

@api_blueprint.route('/db/graph/model/<model>/hops/<hops>')
def getNeighborModels(model, hops):

    cmd = 'MATCH (n:GraphModel) -[*0..{}]- (m:GraphModel {{name:"{}"}}) RETURN DISTINCT n.name'.format(hops, model)
    resp = list()
    with gp.session() as session:
        result = session.run(cmd)         
        for k in result:
            resp.append(k['n.name'])
        

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