#!/bin/bash

HOST=0.0.0.0
PORT=8000

export FLASK_APP=relay
export FLASK_ENV=debug
export FLASK_DEBUG=1
rm -rf *.egg-info
pip install -e .

python ./run.py
