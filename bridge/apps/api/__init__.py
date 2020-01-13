import logging
from flask_restplus import Api
from werkzeug import exceptions
from bridge.apps.common import status
from bridge.apps.common import response as resp


logger = logging.getLogger(__name__)
api = Api(version="1.0.0", title="Bridge REST API for client")


@api.errorhandler
def default_error_handler(e):
    message = "Unhandled exception occurred: {}".format(e)
    logger.exception(message)
    return resp.error(message, status=status.ERROR_BAD_REQUEST)