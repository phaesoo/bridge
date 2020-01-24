from flask import request, current_app as app


def get_config(key):
    val = app.config.get(key)
    if val is None:
        raise ValueError("Invalid config: {}".format(key))
    return val

