from relay.apps.api.restplus import api

from flask import Flask, Blueprint

from relay.db.redis import init_redis
from relay.common.log import init_logger


def create_app(debug=True):
    init_logger(__name__)
    app = Flask(__name__)
    app.config['BUNDLE_ERRORS'] = True

    if debug:
        app.config.from_pyfile("conf/dev.py")
    else:
        raise NotImplementedError
    
    print (app.config)
    # to avoid Runtime error
    with app.app_context():
        init_redis(0)

    # rest api
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    return app
