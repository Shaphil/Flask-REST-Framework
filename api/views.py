from api.infra import APIView


class DemoApi(APIView):

    def get(self):
        return {'message': '.:: Welcome to Flask-REST-Framework ::.'}
