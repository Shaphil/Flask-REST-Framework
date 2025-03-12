from flask.views import MethodView


class APIView(MethodView):
    """
    Generic view for APIs
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
