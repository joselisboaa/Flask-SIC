from flask import Flask
from config import create_default_configs
from api.exception_handler import global_error_handling


def create_app():
    app = Flask(__name__)

    create_default_configs(app)

    # Função para tratamento das exceções lançadas
    global_error_handling(app)

    # O flask identifica o método que retorna a variável app e o executa
    return app
