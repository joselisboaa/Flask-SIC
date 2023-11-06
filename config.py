from dotenv import load_dotenv
from flask_smorest import Api
from flask_migrate import Migrate

from db import db

import os

"""
Nesse módulo teremos as configurações básicas da aplicação
como: configuração de conexão de banco de dados, configurações do swagger,
configurações de migrate e etc.
"""


def create_default_configs(app):
    load_dotenv()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["DEBUG"] = True

    app.config["API_TITLE"] = "SIC API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    Migrate(app=app, db=db, compare_type=True)

    db.init_app(app)
    app.config["API_TITLE"] = "SIC API"

    api = Api(app)
