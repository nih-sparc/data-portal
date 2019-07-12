import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    BLACKFYNN_API_TOKEN = os.environ.get('BLACKFYNN_API_TOKEN', 'local-api-key')
    BLACKFYNN_API_SECRET = os.environ.get('BLACKFYNN_API_SECRET', 'local-secret-key')
    BLACKFYNN_API_HOST = os.environ.get("BLACKFYNN_API_HOST")
    BLACKFYNN_CONCEPTS_API_HOST = os.environ.get("BLACKFYNN_CONCEPTS_API_HOST")
    GRAPHENEDB_BOLT_URL=os.environ.get("GRAPHENEDB_BOLT_URL")
    GRAPHENEDB_BOLT_USER=os.environ.get("GRAPHENEDB_BOLT_USER")
    GRAPHENEDB_BOLT_PASSWORD=os.environ.get("GRAPHENEDB_BOLT_PASSWORD")
    SES_SENDER=os.environ.get("SES_SENDER")
    SES_ARN=os.environ.get("SES_ARN")
    SPARC_PORTAL_AWS_KEY=os.environ.get("SPARC_PORTAL_USER_ID")
    SPARC_PORTAL_AWS_SECRET=os.environ.get("SPARC_PORTAL_USER_SECRET")
    AWS_REGION=os.environ.get("AWS_REGION")