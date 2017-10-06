from .request import Request


def application(environ, start_response):
    request = Request(environ)

    return response

