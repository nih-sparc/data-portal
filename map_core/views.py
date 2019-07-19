# map_core/views.py

#################
#### imports ####
#################

from app import app
from flask import render_template, Blueprint, request, make_response, url_for
from flask import jsonify, send_file, send_from_directory, redirect, abort
import io
import json
from landez.sources import MBTilesReader, ExtractionError
from logger import logger
import os.path
import pathlib
import requests

from .knowledgebase import KnowledgeBase

################
#### config ####
################
 
map_core_blueprint = Blueprint('map_core', __name__, static_folder='../shared/static/dist', template_folder='./static/dist', url_prefix='/map', static_url_path="")

#map_core_blueprint = Blueprint('map_core', __name__, template_folder='./static/dist', url_prefix='/map', static_folder='../shared/static/dist', static_url_path="")

flatmaps_root = os.path.join(map_core_blueprint.root_path, 'flatmaps')

################
#### routes ####
################

@map_core_blueprint.route('/')
def index():
    return render_template('maps.html')

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

################
### flatmaps ###
################

@map_core_blueprint.route('flatmap/')
def maps():
    maps = []
    for path in pathlib.Path(flatmaps_root).iterdir():
        mbtiles = os.path.join(flatmaps_root, path, 'index.mbtiles')
        if os.path.isdir(path) and os.path.exists(mbtiles):
            reader = MBTilesReader(mbtiles)
            source_row = reader._query("SELECT value FROM metadata WHERE name='source';").fetchone()
            if source_row is not None:
                maps.append({ 'id': path.name, 'source': source_row[0] })
    return jsonify(maps)

@map_core_blueprint.route('flatmap/<string:map>/')
def map(map):
    filename = os.path.join(flatmaps_root, map, 'index.json')
    return send_file(filename)

@map_core_blueprint.route('flatmap/<string:map>/style')
def style(map):
    filename = os.path.join(flatmaps_root, map, 'style.json')
    return send_file(filename)

@map_core_blueprint.route('flatmap/<string:map>/annotations')
def map_annotations(map):
    mbtiles = os.path.join(flatmaps_root, map, 'index.mbtiles')
    reader = MBTilesReader(mbtiles)
    rows = reader._query("SELECT value FROM metadata WHERE name='annotations';").fetchone()
    if rows is None:
        annotations = {}
    else:
        annotations = json.loads(rows[0])
    return jsonify(annotations)

@map_core_blueprint.route('flatmap/<string:map>/images/<string:image>')
def map_background(map, image):
    filename = os.path.join(flatmaps_root, map, 'images', image)
    return send_file(filename)

@map_core_blueprint.route('flatmap/<string:map>/mvtiles/<int:z>/<int:x>/<int:y>')
def vector_tiles(map, z, y, x):
    try:
        mbtiles = os.path.join(flatmaps_root, map, 'index.mbtiles')
        reader = MBTilesReader(mbtiles)
        return send_file(io.BytesIO(reader.tile(z, x, y)), mimetype='application/octet-stream')
    except ExtractionError:
        pass
    return ('', 204)

@map_core_blueprint.route('flatmap/<string:map>/tiles/<string:layer>/<int:z>/<int:x>/<int:y>')
def image_tiles(map, layer, z, y, x):
    try:
        mbtiles = os.path.join(flatmaps_root, map, '{}.mbtiles'.format(layer))
        reader = MBTilesReader(mbtiles)
        return send_file(io.BytesIO(reader.tile(z, x, y)), mimetype='image/png')
    except ExtractionError:
        pass
    return ('', 204)

@map_core_blueprint.route('query', methods=['POST'])
def kb_query():
    query = request.get_json()
    try:
        with KnowledgeBase(os.path.join(flatmaps_root, 'KnowledgeBase.sqlite')) as graph:
            return jsonify(graph.query(query.get('sparql')))
    except RuntimeError:
        abort(404, 'Cannot open knowledge base')
