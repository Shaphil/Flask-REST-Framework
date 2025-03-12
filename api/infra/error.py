from flask import current_app as app
from flask import jsonify


class APINotImplementedException(Exception):
    """Base API exception."""
    code = 500
    message = "API Not Implemented"


@app.errorhandler(APINotImplementedException)
def handle_api_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = jsonify({
        'message': e.message,
        'code': e.code,
    })
    return response
