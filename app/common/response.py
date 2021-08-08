from typing import Union
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

# status 200
class Success(Exception):

    def __init__(self, message):
        self.data = message

# status 201
class Created(Exception):

    def __init__(self, message):
        self.data = message

# status 204
class SuccessNoContent(Exception):

    def __init__(self):
        self.data = ''

# status 400
class BadRequest(Exception):

    def __init__(self, message):
        self.data = {
            'message': message
        }

# status 404
class NotFound(Exception):

    def __init__(self):
        self.data = {
            'message': 'data not found'
        }

# status 5xx
class InternalServerError(Exception):

    def __init__(self, error):
        self.data = {
            'error': error
        }

def common_response(
    data:Union[Success, Created, BadRequest, InternalServerError]
)->Response:
    if type(data) == Success:
        return Response(data.data, status=HTTP_200_OK)
    if type(data) == Created:
        return Response(data.data, status=HTTP_201_CREATED)
    if type(data) == SuccessNoContent:
        return Response(data.data, status=HTTP_204_NO_CONTENT)
    if type(data) == BadRequest:
        return Response(data.data, status=HTTP_400_BAD_REQUEST)
    if type(data) == NotFound:
        return Response(data.data, status=HTTP_404_NOT_FOUND)
    if type(data) == InternalServerError:
        return Response(data.data, status=HTTP_500_INTERNAL_SERVER_ERROR)
    return Exception("Status not found")
