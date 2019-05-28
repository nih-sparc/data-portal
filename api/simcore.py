import json
from pprint import pprint

def read_studies():
    with open('static/simcore_data/template-projects.isan.json') as f:
        studies = json.load(f)
    return studies

def init_sim_db(gp):
    studies = read_studies()

    create_cmd = """
    UNWIND {json} AS study
    MERGE (s:Study {uuid: study.uuid})
    SET s = study
    RETURN s
    """

    with gp.session() as session:
        session.run(create_cmd, {"json": studies})

    return 1