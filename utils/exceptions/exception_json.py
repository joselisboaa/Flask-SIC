from flask import make_response, jsonify


class ExceptionJsonSchema(Exception):
    def __init__(self, message, details, status_code, http_method):
        self.message = message
        self.details = details
        self.status_code = status_code
        self.http_method = http_method

    def to_json(self):
        return make_response(
            jsonify(
                {
                    "message": self.message,
                    "details": self.details,
                    "status_code": self.status_code,
                    "http_method": self.http_method.value,
                }
            ),
            self.status_code,
        )
