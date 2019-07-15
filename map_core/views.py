# map_core/views.py

# Imports
import os
import json
import requests

from flask import render_template, Blueprint, request, make_response, redirect

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


@map_core_blueprint.route('staging_model/<path:p>')
def getStagingModel(p):
    url = 'https://staging.physiomeproject.org/workspace/{0}'.format(p)
    return get_response_from_remote(url)


@map_core_blueprint.route('scaffoldmaker/<path:p>')
def scaffoldmakerproxy(p = ''):
    url = 'http://localhost:6565/{0}?{1}'.format(p, str(request.query_string, 'utf-8'))
    return get_response_from_remote(url)


@map_core_blueprint.route('knowledgebase/<path:data_set>')
def knowledge_base_proxy(data_set=''):
    query_string = ensure_string(request.query_string)
    url = 'https://scicrunch.org/api/1/dataservices/federation/data/{0}?{1}'.format(data_set, query_string, 'utf-8')
    return get_response_from_remote(url)


@map_core_blueprint.route('biolucida/<path:api_method>', methods=['GET', 'POST'])
def biolucida_client_proxy(api_method=''):
    url = 'https://sparc.biolucida.net/api/v1/{0}'.format(api_method, 'utf-8')

    if request.method == 'POST':
        request_data = json.loads(request.data)

        if api_method == 'authenticate':
            request_data['username'] = os.environ['BIOLUCIDA_USEERNAME']
            request_data['password'] = os.environ['BIOLUCIDA_PASSWORD']

        return post_response_from_remote(url, data=request_data)
    else:
        return get_response_from_remote(url, headers={'token': request.headers['token']})


def get_response_from_remote(url, headers=None):
    try:
        session = requests.Session()
        if headers is not None:
            session.headers.update(headers)

        r = session.get(url, cookies=request.cookies)
    except Exception as e:
        return "proxy service error: " + str(e), 503
    resp = make_response(r.content)
    if r.cookies.get('sessionid'):
        resp.set_cookie('sessionid', r.cookies.get('sessionid'))
    return resp


def post_response_from_remote(url, data=None):
    try:
        session = requests.Session()
        r = session.post(url, data=data)
    except Exception as e:
        return "proxy service error: " + str(e), 503

    resp = make_response(r.content)

    if r.cookies.get('sessionid'):
        resp.set_cookie('sessionid', r.cookies.get('sessionid'))

    return resp


def ensure_string(data):
    if type(data) == bytes:
        string = data.decode()
    else:
        string = data

    return string
