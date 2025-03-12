from api.infra import APIView


class DemoApi(APIView):
    message = '.:: Welcome to Flask-REST-Framework ::.'

    def get(self):
        return {'message': self.message}
