from .views import views

from flask import Flask
import os 

LOCAL_FOLDER = "templates"

here = os.path.dirname(os.path.abspath(__file__))
templates_folder = os.path.join(here, LOCAL_FOLDER)

class FlaskWeb:
    def __init__(self, debug=False, port = 9999):
        self.app = Flask('application', template_folder=templates_folder)
        self.app.register_blueprint(views, url_prefix="/")
        self.app.run(debug=debug, port=port)

    def simple_listing(self):
        pass


