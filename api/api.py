# api/api.py

#################
#### imports ####
#################
from client import MockSparcPortalApiClient
from model import SparcPortalSearchParameters
from serializer import PaginatedDatasetResponseSchema, PaginatedFileResponseSchema, DatasetSchema, ContactRequestSchema
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
client = MockSparcPortalApiClient()

@api_blueprint.route("/contact", methods=["POST"])
def contact():
    data = json.loads(request.data)
    contact_request = ContactRequestSchema().load(data).data

    client.send_contact_request(
        name=contact_request["name"],
        email=contact_request["email"],
        message=contact_request["message"]
    )

    return ''

#########################
#### DAT-CORE routes ####
#########################

# Returns a list of public datasets from 
@api_blueprint.route('/datasets')
def discover():
    resp = bf._api._get('/consortiums/1/datasets')
    return json.dumps(resp)

@api_blueprint.route('/search/dataset')
def search_dataset():
    response = client.search_datasets(
        SparcPortalSearchParameters(
            limit=10,
            offset=0,
            terms=[],
            tags=[]
        )
    )

    marshalled = PaginatedDatasetResponseSchema().dump(response)
    return json.dumps(marshalled.data)

@api_blueprint.route("/search/file")
def search_file():
    response = client.search_files(
        SparcPortalSearchParameters(
            limit=10,
            offset=0,
            terms=[],
            tags=[]
        )
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
