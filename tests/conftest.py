import os
import pytest
import tempfile
from relay import create_app, create_sio
from relay.apps.socketio.namespaces.feeder import FeederNamespace


@pytest.fixture(scope="session")
def client():
    app = create_app(debug=True)
    # socket io
    sio = create_sio(istest=True)
    sio.init_app(app)
    app.config["TESTING"] = True

    return sio.test_client(app)
