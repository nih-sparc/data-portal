from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from config import Config

app = Flask(__name__, static_folder="./static", template_folder="./templates")
ma = Marshmallow(app)

with app.app_context():
    from logger import logger

import routes