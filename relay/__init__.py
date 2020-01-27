from relay.apps.api.restplus import api

from flask import Flask, Blueprint
from flask_socketio import SocketIO, emit

from relay.db.redis import init_redis
from relay.common.log import init_logger
from relay.apps.socketio.namespaces.feeder import FeederNamespace


def create_app(debug=True):
    init_logger(__name__)
    app = Flask(__name__)
    app.config['BUNDLE_ERRORS'] = True

    if debug:
        app.config.from_pyfile("conf/dev.py")
    else:
        raise NotImplementedError
    
    # to avoid Runtime error
    with app.app_context():
        init_redis(5)

    # rest api
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    return app


def create_sio(istest=False):
    # socket io
    if istest is True:
        socketio = SocketIO()
    else:
        socketio = SocketIO(message_queue='redis://')
    socketio.on_namespace(FeederNamespace("/feeder"))
    return socketio