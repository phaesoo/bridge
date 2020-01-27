#!/bin/env python
from argparse import ArgumentParser
from relay import create_app, create_sio


def pass_options():
    parser = ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("-p", "--port", type=int, default=8000)
    parser.add_argument("-d", "--debug", type=bool, default=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = pass_options()

    # flask app
    app = create_app(debug=args.debug)
    # socketio
    sio = create_sio()
    sio.init_app(app)
    sio.run(app, host=args.host, port=args.port)