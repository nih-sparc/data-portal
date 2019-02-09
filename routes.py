from flask import jsonify, render_template, request

from app import app
from logger import logger
from blackfynn import Blackfynn

bf = None

@app.before_first_request
def connect_to_blackfynn():
    global bf
    #bf = Blackfynn(
    #    api_token=Config.BLACKFYNN_API_TOKEN,
    #    api_secret=Config.BLACKFYNN_API_SECRET,
    #    env_override=False,
    #    host=Config.BLACKFYNN_API_HOST,
    #    concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
    #)


@app.route('/')
def home():
    return render_template("index.html")
    
