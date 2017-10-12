from framework import Request
from framework import get_404_not_found


def application(environ, start_response):
    debug = False
    request = Request(environ)
    response = get_404_not_found(request, start_response, True)
    return response

