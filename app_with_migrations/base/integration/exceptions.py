from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

class UseCaseIsNotSetException(APIException):
    status_code = 500
    default_detail = 'use case is not set'
    default_code = 'not_set'


class BadParameterException(APIException):
    status_code = 400
    default_detail = 'bad parameter'
    default_code = 'bad_parameter'
    
class ErrorWithMessage(APIException):
    status_code = 420
    default_detail = 'result: error with message'
    default_code = 'error_with_message'

    def __init__(self, error_message: str, error_message_full: str, detail=None, code=None):
        super().__init__(detail, code)

        self.error_message = error_message
        self.error_message_full = error_message_full


def error_with_message_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and isinstance(exc, ErrorWithMessage):
        response.data['error_message'] = exc.error_message
        response.data['error_message_full'] = exc.error_message_full

    return response
