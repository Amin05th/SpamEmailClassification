from flask import Flask, Blueprint, redirect
import settings
from Flask_API.api.myapi import api
from Flask_API.api.endpoints.spamemails import namespace as spamnamespace
from Flask_API.api.database.db import db

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/api")


def config_settings(app):
    app.config["SWAGGER_UI_DOC_EXPANSION"] = settings.RESTPLUS_SWAGGER_EXPANSION
    app.config["RESTPLUS_VALIDATE"] = settings.RESTPLUS_VAL
    app.config["RESTPLUS_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODS"] = settings.SQLALCHEMY_TRACK_MODS


def init(app):
    config_settings(app)
    blueprint = Blueprint("spam emails", __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.add_namespace(spamnamespace)
    app.register_blueprint(blueprint)
    db.init_app(app)


def main():
    init(app)
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG, threaded=settings.FLASK_THREADED)


if __name__ == '__main__':
    main()
