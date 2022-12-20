from flask.views import MethodView


class APIView(MethodView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch_request(self, *args, **kwargs):
        return super().dispatch_request(*args, **kwargs)
