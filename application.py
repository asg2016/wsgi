from framework.requests import Request
from framework.helpers import get_404_not_found


def application(environ, start_response):
    debug = False
    request = Request(environ)
    response = get_404_not_found(request, start_response, True)
    return response

