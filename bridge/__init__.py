from bridge.apps.api.restplus import api

from flask import Flask, Blueprint


#from app.db.database import init_db
from bridge.apps.common.log import init_logger


def create_app(debug=True):
    init_logger(__name__)
    app = Flask(__name__)
    app.config['BUNDLE_ERRORS'] = True

    if debug:
        app.config.from_pyfile("./configs/dev.py")
    else:
        raise NotImplementedError

    ## to avoid Runtime error
    #with app.app_context():
    #    init_db()

    # rest api
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    return app
