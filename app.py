#################
#### imports ####
#################
 
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import Config
from blackfynn import Blackfynn
 
################
#### config ####
################

# Change jinja variable notation to support Vue app
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))

app = CustomFlask(__name__, static_folder="./static", template_folder="./templates")  # This replaces your existing "app = Flask(__name__)"

# app = Flask(__name__, static_folder="./static", template_folder="./templates")
ma = Marshmallow(app)
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

with app.app_context():
    from logger import logger
 
####################
#### blueprints ####
####################
 
from dat_core.views import dat_core_blueprint
from map_core.views import map_core_blueprint
from sim_core.views import sim_core_blueprint
from dashboard.views import dashboard_blueprint

# register the blueprints
app.register_blueprint(map_core_blueprint)
app.register_blueprint(dat_core_blueprint)
app.register_blueprint(sim_core_blueprint)
app.register_blueprint(dashboard_blueprint)