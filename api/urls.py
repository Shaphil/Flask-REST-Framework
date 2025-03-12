from flask import current_app as app

from api.views import DemoApi

path = app.add_url_rule

path('/api/demo', view_func=DemoApi.as_view('demo'))
