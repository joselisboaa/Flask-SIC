from flask import make_response, jsonify
from sqlalchemy.exc import SQLAlchemyError

from utils.exceptions import (
    NotFoundException
)


def global_error_handling(app):
    @app.errorhandler(NotFoundException)
    def not_found_constraint_error(error):
        return NotFoundException(
            message=error.message,
            http_method=error.http_method,
            status_code=error.status_code,
            details=error.details,
        ).to_json()

    @app.errorhandler(SQLAlchemyError)
    def sqlalchemy_error(error):
        return make_response(jsonify({"details": error, "message": "Erro no servidor."}), 500)
