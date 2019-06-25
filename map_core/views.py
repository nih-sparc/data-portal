# map_core/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint, request,make_response, url_for, jsonify, send_from_directory, redirect
from logger import logger
import requests

################
#### config ####
################
 
map_core_blueprint = Blueprint('map_core', __name__, template_folder='templates', url_prefix='/map', static_folder='static')

################
#### routes ####
################
 
@map_core_blueprint.route('/')
def index():
    return render_template('map_core.html')

@map_core_blueprint.route('models/<path:p>')
def getModels(p):
    url = 'map/static/models/{0}'.format(p)
    #print(url_for('static', filename=url))
    return redirect(url)

def getResponseFromRemote(url):
    try:
        session = requests.Session()
        r = session.get(url, cookies = request.cookies)
    except Exception as e:
        return "proxy service error: " + str(e), 503
    resp = make_response(r.content)
    if r.cookies.get('sessionid'):
        resp.set_cookie('sessionid', r.cookies.get('sessionid'))
    return resp

@map_core_blueprint.route('staging_model/<path:p>')
def getStagingModel(p):
    url = 'https://staging.physiomeproject.org/workspace/{0}'.format(p)
    return getResponseFromRemote(url)

@map_core_blueprint.route('scaffoldmaker/<path:p>')
def scaffoldmakerproxy(p = ''):
    url = 'http://localhost:6565/{0}?{1}'.format(p, str(request.query_string, 'utf-8'))
    return getResponseFromRemote(url)
