from flask.views import MethodView

from .error import APINotImplementedException


class APIView(MethodView):
    """
    Generic view for APIs
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        raise APINotImplementedException()

    def post(self):
        raise APINotImplementedException()

    def put(self):
        raise APINotImplementedException()

    def patch(self):
        raise APINotImplementedException()

    def delete(self):
        raise APINotImplementedException()
