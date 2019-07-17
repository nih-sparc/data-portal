# api/api.py

#################
#### imports ####
#################
import boto3

from .email_sender import EmailSender
from .client import MockSparcPortalApiClient
from .model import SparcPortalSearchParameters
from .serializer import PaginatedDatasetResponseSchema, PaginatedFileResponseSchema, DatasetSchema, ContactRequestSchema
from app import app
from flask import render_template, Blueprint, request, jsonify
from logger import logger
from blackfynn import Blackfynn
from config import Config
from flask_marshmallow import Marshmallow
from neo4j import GraphDatabase, basic_auth
import json
import urllib
import requests

################
#### config ####
################

api_blueprint = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')

gp = None
bf = None
ma = Marshmallow(app)
client = MockSparcPortalApiClient()
email_sender = EmailSender()

@api_blueprint.route("/contact", methods=["POST"])
def contact():
    data = json.loads(request.data)
    contact_request = ContactRequestSchema().load(data).data

    name = contact_request["name"]
    email = contact_request["email"]
    message = contact_request["message"]

    email_sender.send_email(name, email, message)

    return json.dumps({ "status": "sent" })

@app.before_first_request
def connect_to_graphenedb():
    global gp
    # graphenedb_url = Config.GRAPHENEDB_BOLT_URL
    # graphenedb_user = Config.GRAPHENEDB_BOLT_USER
    # graphenedb_pass = Config.GRAPHENEDB_BOLT_PASSWORD
    # gp = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))

    # init_sim_db(gp)

#########################
#### DAT-CORE routes ####
#########################

# Returns a list of public datasets from 
@api_blueprint.route('/datasets')
def discover():
    resp = bf._api._get('/consortiums/1/datasets')
    return json.dumps(resp)

@api_blueprint.route('/dataset/<int:id>')
def dataset(id):
    response = client.retrieve_dataset(id)
    marshalled = DatasetSchema().dump(response)

    return json.dumps(marshalled.data)

@api_blueprint.route('/search/dataset')
def search_dataset():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    terms = request.args.getlist('terms')
    tags = request.args.getlist('tags')

    response = client.search_datasets(
        SparcPortalSearchParameters(limit, offset, terms, tags)
    )

    marshalled = PaginatedDatasetResponseSchema().dump(response)
    return json.dumps(marshalled.data)

@api_blueprint.route("/search/file")
def search_file():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    terms = request.args.getlist('terms')
    tags = request.args.getlist('tags')

    response = client.search_files(
        SparcPortalSearchParameters(limit, offset, terms, tags)
    )

    marshalled = PaginatedFileResponseSchema().dump(response)
    return json.dumps(marshalled.data)

@api_blueprint.route("/featured")
def featured():
    response = client.retrieve_featured_datasets()
    marshalled = DatasetSchema().dump(response, many=True)

    return json.dumps(marshalled.data)

#########################
#### MAP-CORE routes ####
#########################


#########################
#### SIM-CORE routes ####
#########################

import logging

tags = 'tags=simcore'

@api_blueprint.route('/sim/dataset')
def sim_datasets():
    if request.method == 'GET':
        req = requests.get('{}/datasets?{}'.format(Config.DISCOVER_API_HOST, tags))
        json = req.json()
        return jsonify(json)

@api_blueprint.route('/sim/search-dataset')
def sim_search_datasets():
    if request.method == 'GET':
        query = request.args.get('query')
        req = requests.get('{}/search/datasets?query={}'.format(Config.DISCOVER_API_HOST, query))
        json = req.json()
        # Filter only datasets with tag 'simcore'
        json['datasets'] = filter(lambda dataset: ('simcore' in dataset.get('tags', [])), json.get('datasets', []))
        return jsonify(json)

@api_blueprint.route('/sim/dataset/<id>')
def sim_dataset(id):
    if request.method == 'GET':
        req = requests.get('{}/datasets/{}'.format(Config.DISCOVER_API_HOST, id))
        json = req.json()
        inject_markdown(json)
        inject_template_data(json)
        return jsonify(json)

def inject_markdown(resp):
    if 'readme' in resp:
        mark_req = requests.get(resp.get('readme'))
        resp['markdown'] = mark_req.text

def inject_template_data(resp):
    import boto3
    from botocore.exceptions import ClientError
    import json

    id = resp.get('id')
    version = resp.get('version')
    if (id is None or version is None):
        return

    try:
        s3_client = boto3.Session().client('s3', region_name='us-east-1')
        response = s3_client.get_object(Bucket='blackfynn-discover-use1',
                                        Key='{}/{}/packages/template.json'.format(id, version),
                                        RequestPayer='requester')
    except ClientError as e:
        logging.error(e)
        return

    template = response['Body'].read()

    try:
        template_json = json.loads(template)
    except ValueError as e:
        logging.error(e)
        return

    resp['study'] = {'uuid': template_json.get('uuid'),
                     'name': template_json.get('name'),
                     'description': template_json.get('description')}
