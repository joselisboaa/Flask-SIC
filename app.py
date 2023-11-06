from flask import Flask
from config import create_default_configs


def create_app():
    app = Flask(__name__)

    create_default_configs(app)

    # O flask identifica o método que retorna a variável app e o executa
    return app
