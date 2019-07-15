# map_core/views.py

# Imports
from app import app
from flask import render_template, Blueprint, request, make_response, redirect
from logger import logger
import requests

# Config
map_core_blueprint = Blueprint('map_core', __name__, template_folder='templates', url_prefix='/map', static_folder='static')

# Routes
@map_core_blueprint.route('/')
def index():
    return render_template('map_core.html')


@map_core_blueprint.route('8ed83a516242675649285ff523ffddb6.svg')
def getLogo():
    url = 'map/static/8ed83a516242675649285ff523ffddb6.svg'
    return redirect(url)


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


@map_core_blueprint.route('scaffoldmaker/<path:p>')
def scaffoldmakerproxy(p = ''):
    url = 'http://localhost:6565/{0}?{1}'.format(p, str(request.query_string, 'utf-8'))
    return get_response_from_remote(url)
