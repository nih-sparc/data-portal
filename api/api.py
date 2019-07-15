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

gp = None
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
