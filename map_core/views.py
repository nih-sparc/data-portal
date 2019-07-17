# map_core/views.py

# Imports
from app import app
from flask import render_template, Blueprint, request, make_response, redirect
from logger import logger
import requests


################
#### config ####
################
 
map_core_blueprint = Blueprint('map_core', __name__, static_folder='../shared/static/dist', template_folder='./static/dist', url_prefix='/map', static_url_path="")

# Routes
@map_core_blueprint.route('/')
def index():
    return render_template('maps.html')

@map_core_blueprint.route('models/<path:p>')
def getModels(p):
    url = 'map/static/models/{0}'.format(p)
    return redirect(url)


def get_response_from_remote(url):
    try:
        session = requests.Session()
        r = session.get(url, cookies=request.cookies)
    except Exception as e:
        return "proxy service error: " + str(e), 503
    resp = make_response(r.content)
    if r.cookies.get('sessionid'):
        resp.set_cookie('sessionid', r.cookies.get('sessionid'))
    return resp


@map_core_blueprint.route('staging_model/<path:p>')
def getStagingModel(p):
    url = 'https://staging.physiomeproject.org/workspace/{0}'.format(p)
    return get_response_from_remote(url)


@map_core_blueprint.route('exfetch/<path:p>')
def scaffoldmakerproxy(p = ''):
    url = '{0}?{1}'.format(p, str(request.query_string, 'utf-8'))
    return get_response_from_remote(url)

