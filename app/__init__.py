from flask import Flask, Blueprint
from app.api.v1.Views.views import PartiesResource
from app.api.v1.Views.views import parties


def create_app():

    app = Flask(__name__)

    app.register_blueprint(parties, url_prefix='/api/v1/')

    return app