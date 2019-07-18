import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    AWS_REGION=os.environ.get("AWS_REGION")
    BLACKFYNN_API_HOST = os.environ.get("BLACKFYNN_API_HOST")
    BLACKFYNN_API_SECRET = os.environ.get('BLACKFYNN_API_SECRET', 'local-secret-key')
    BLACKFYNN_API_TOKEN = os.environ.get('BLACKFYNN_API_TOKEN', 'local-api-key')
    BLACKFYNN_EMBARGO_TEAM_ID = os.environ.get("BLACKFYNN_EMBARGO_TEAM_ID")
    DISCOVER_API_HOST=os.environ.get('DISCOVER_API_HOST', 'https://api.blackfynn.io/discover')
    GRAPHENEDB_BOLT_PASSWORD=os.environ.get("GRAPHENEDB_BOLT_PASSWORD")
    GRAPHENEDB_BOLT_URL=os.environ.get("GRAPHENEDB_BOLT_URL")
    GRAPHENEDB_BOLT_USER=os.environ.get("GRAPHENEDB_BOLT_USER")
    MONGODB_COLLECTION="sparc-embargo"
    MONGODB_NAME="sparc-embargo"
    MONGODB_URI=os.environ.get("MONGODB_URI")
    SES_ARN=os.environ.get("SES_ARN")
    SES_SENDER=os.environ.get("SES_SENDER")
    SPARC_PORTAL_AWS_KEY=os.environ.get("SPARC_PORTAL_USER_ID")
    SPARC_PORTAL_AWS_SECRET=os.environ.get("SPARC_PORTAL_USER_SECRET")
