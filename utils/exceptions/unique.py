from utils.exceptions.exception_json import ExceptionJsonSchema
from utils.enums import Http


class UniqueException(ExceptionJsonSchema):
    def __init__(self, message: str, details: str, http_method: Http, status_code=400):
        super().__init__(message, details, status_code, http_method)
