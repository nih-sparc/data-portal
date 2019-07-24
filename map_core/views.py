# map_core/views.py

# Imports
import os
import json
import requests

from flask import render_template, Blueprint, request, make_response, redirect

import sys
import logging


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger("flask_mapcore")

# Config
map_core_blueprint = Blueprint('map_core', __name__, static_folder='../shared/static/dist', template_folder='./static/dist', url_prefix='/map', static_url_path="")

# Routes
@map_core_blueprint.route('/')
def index():
    return render_template('maps.html')

@map_core_blueprint.route('models/<path:p>')
def getModels(p):
    url = 'map/static/models/{0}'.format(p)
    return redirect(url)


@map_core_blueprint.route('staging_model/<path:p>')
def getStagingModel(p):
    url = 'https://staging.physiomeproject.org/workspace/{0}'.format(p)
    return get_response_from_remote(url)


@map_core_blueprint.route('exfetch/<path:p>')
def scaffoldmakerproxy(p = ''):
    url = '{0}?{1}'.format(p, str(request.query_string, 'utf-8'))
    return get_response_from_remote(url)


@map_core_blueprint.route('knowledgebase/<path:data_set>')
def knowledge_base_proxy(data_set=''):
    query_string = ensure_string(request.query_string)
    url = 'https://scicrunch.org/api/1/dataservices/federation/data/{0}?{1}&{2}'.format(data_set, query_string, 'key={}'.format(os.environ['KNOWLEDGEBASE_KEY']), 'utf-8')
    return get_response_from_remote(url)


@map_core_blueprint.route('biolucida/<path:api_method>', methods=['GET', 'POST'])
def biolucida_client_proxy(api_method=''):
    url = 'https://sparc.biolucida.net/api/v1/{0}'.format(api_method, 'utf-8')

    if request.method == 'POST':
        request_data = json.loads(ensure_string(request.data))

        if api_method == 'authenticate/':
            request_data['username'] = os.environ['BIOLUCIDA_USERNAME'] if 'BIOLUCIDA_USERNAME' in os.environ else 'major_user'
            request_data['password'] = os.environ['BIOLUCIDA_PASSWORD'] if 'BIOLUCIDA_PASSWORD' in os.environ else 'password'

        return post_response_from_remote(url, data=request_data)
    else:
        return get_response_from_remote(url, headers={'token': request.headers['token']})


@map_core_blueprint.route('osparc/<int:mode>/<float:level>', methods=['GET'])
def osparc_client_proxy(mode=1, level=0.5):
    study_id = '194bb264-a717-11e9-9dff-02420aff2767'
    web_hook = ''
    # url = 'https://osparc.io/study/194bb264-a717-11e9-9dff-02420aff2767?stimulation_mode=1&stimulation_level=0.5'
    webhook = 'http://163.47.115.91:5000/osparc_webhook?simulation_id=123456'
    url = 'https://osparc.io/study/{0}?stimulation_mode={1}&stimulation_level={2}&webhook_done={3}'.format(study_id, mode, level, webhook, 'utf-8')
    print(url)
    logger.info(mode)
    logger.info(level)
    logger.info(url)
    print("==================")
    # print(dir(request))
    # request.set_cookie("user", value="h.sorby@auckland.ac.nz")
    # request.set_cookie("API_SESSION", value="gAAAAABdLkIw88gtEgcMAHGmlnTHafVmsAkAJRVWFSlT7j9kpDo2Jxtknxr9lQYcSnCC5UGo9IdzzyMEOPhijLvDqdyo7lEwznXmz0ZEubecPL9QohDHcUyZzMfUif8WNjZv4MXEaIKIWwfppbfSbrJBPqtewjVLSsc1PAF5UahV77qA8nyxaAip1qR1bSj-JJiBkkV4LnmP")
    # print("==================")
    # print(dir(request))
    # print(request.cookies)
    return get_response_from_remote(url)


@map_core_blueprint.route('osparc_webhook/', methods=['GET', 'POST'])
def osparc_webhook():
    print(request.get_json())
    if request.method == 'POST':
        print('received a post')
    else:
        print('received a get')


def get_response_from_remote(url, headers=None):
    try:
        session = requests.Session()
        if headers is not None:
            session.headers.update(headers)

        my_cookies = request.cookies
        # my_cookies = {}
        # my_cookies["user"] = "h.sorby@auckland.ac.nz"
        # my_cookies["API_SESSION"] = "gAAAAABdLkIw88gtEgcMAHGmlnTHafVmsAkAJRVWFSlT7j9kpDo2Jxtknxr9lQYcSnCC5UGo9IdzzyMEOPhijLvDqdyo7lEwznXmz0ZEubecPL9QohDHcUyZzMfUif8WNjZv4MXEaIKIWwfppbfSbrJBPqtewjVLSsc1PAF5UahV77qA8nyxaAip1qR1bSj-JJiBkkV4LnmP"
        r = session.get(url, cookies=my_cookies)
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
