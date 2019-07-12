# map_core/views.py

# Imports
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

# Config
map_core_blueprint = Blueprint('map_core', __name__, template_folder='templates', url_prefix='/map', static_folder='static')

flatmaps_root = os.path.join(map_core_blueprint.root_path, 'flatmaps')

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


# Flatmaps
@map_core_blueprint.route('flatmap/')
def maps():
    flatmap_list = []
    for tile_dir in pathlib.Path(flatmaps_root).iterdir():
        mbtiles = os.path.join(flatmaps_root, tile_dir, 'index.mbtiles')
        if os.path.isdir(tile_dir) and os.path.exists(mbtiles):
            reader = MBTilesReader(mbtiles)
            source_row = reader._query("SELECT value FROM metadata WHERE name='source';").fetchone()
            if source_row is not None:
                flatmap = { 'id': path.name, 'source': source_row[0] }
                created = reader._query("SELECT value FROM metadata WHERE name='created';").fetchone()
                if created is not None:
                    flatmap['created'] = created[0]
                describes = reader._query("SELECT value FROM metadata WHERE name='describes';").fetchone()
                if describes is not None:
                    flatmap['describes'] = describes[0]
                flatmap_list.append(flatmap)
    return jsonify(flatmap_list)


@map_core_blueprint.route('flatmap/<string:map_path>/')
def map(map_path):
    filename = os.path.join(flatmaps_root, map_path, 'index.json')
    return send_file(filename)


@map_core_blueprint.route('flatmap/<string:map_path>/style')
def style(map_path):
    filename = os.path.join(flatmaps_root, map_path, 'style.json')
    return send_file(filename)


@map_core_blueprint.route('flatmap/<string:map_path>/annotations')
def map_annotations(map_path):
    mbtiles = os.path.join(flatmaps_root, map_path, 'index.mbtiles')
    reader = MBTilesReader(mbtiles)
    rows = reader._query("SELECT value FROM metadata WHERE name='annotations';").fetchone()
    if rows is None:
        annotations = {}
    else:
        annotations = json.loads(rows[0])
    return jsonify(annotations)


@map_core_blueprint.route('flatmap/<string:map_path>/images/<string:image>')
def map_background(map_path, image):
    filename = os.path.join(flatmaps_root, map_path, 'images', image)
    return send_file(filename)


@map_core_blueprint.route('flatmap/<string:map_path>/mvtiles/<int:z>/<int:x>/<int:y>')
def vector_tiles(map_path, z, y, x):
    try:
        mbtiles = os.path.join(flatmaps_root, map_path, 'index.mbtiles')
        reader = MBTilesReader(mbtiles)
        return send_file(io.BytesIO(reader.tile(z, x, y)), mimetype='application/octet-stream')
    except ExtractionError:
        pass
    return '', 204


@map_core_blueprint.route('flatmap/<string:map_path>/tiles/<string:layer>/<int:z>/<int:x>/<int:y>')
def image_tiles(map_path, layer, z, y, x):
    try:
        mbtiles = os.path.join(flatmaps_root, map_path, '{}.mbtiles'.format(layer))
        reader = MBTilesReader(mbtiles)
        return send_file(io.BytesIO(reader.tile(z, x, y)), mimetype='image/png')
    except ExtractionError:
        pass
    return '', 204


@map_core_blueprint.route('query', methods=['POST'])
def kb_query():
    query = request.get_json()
    try:
        with KnowledgeBase(os.path.join(flatmaps_root, 'KnowledgeBase.sqlite')) as graph:
            return jsonify(graph.query(query.get('sparql')))
    except RuntimeError:
        abort(404, 'Cannot open knowledge base')
