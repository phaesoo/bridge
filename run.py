#!/bin/env python
from argparse import ArgumentParser
from flask_socketio import SocketIO, emit
from relay import create_app
from relay.apps.socketio.namespaces.feeder import FeederNamespace


def pass_options():
    parser = ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("-p", "--port", type=int, default=8000)
    parser.add_argument("-d", "--debug", type=bool, default=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = pass_options()

    app = create_app(debug=args.debug)
    # socket io
    socketio = SocketIO(app)
    socketio.on_namespace(FeederNamespace("/feeder"))
    socketio.run(app, host=args.host, port=args.port)