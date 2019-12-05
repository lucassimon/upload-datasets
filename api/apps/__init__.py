# -*- coding: utf-8 -*-

from flask import Flask, jsonify

# Third
from .configs import config
from flask_cors import CORS

# Apps
from apps.messages import Messages

# Local
# Realize a importação da função que configura a api
from .api import configure_api
from .db import db
from .celery_utils import init_celery
from .celery import celery


def create_app(config_name, **kwargs):
    app = Flask("dataset")

    app.config.from_object(config[config_name])

    if kwargs.get("celery"):
        init_celery(celery, app)

    @app.after_request
    def apply_caching(response):
        response.headers["X-DEV"] = "Created with love."
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        resp = jsonify({"status": 404, "message": Messages.RESOURCE_NOT_FOUND.value})
        resp.status_code = 404
        return resp

    CORS(app, resources={r"/*": {"origins": "*"}})

    # Configure MongoEngine
    db.init_app(app)

    # executa a chamada da função de configuração
    configure_api(app)

    return app
