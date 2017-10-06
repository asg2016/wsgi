from urllib.parse import parse_qs


def application(environ, start_response):
    global request
    global response
    start_response(response['status'], [('Content-type',response['content_type'])])
    request = Request(environ)
    return response


def not_found():
    response.status = '404 Not Found'
    response.content_type = 'text/plain'


class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.request_data = None
        self._parse_request_data()

    def _parse_request_data(self):
        if self.is_get():
            self.request_data = parse_qs(self.environ['QUERY_STRING'])
        elif self.is_post():
            try:
                request_body_size = int(self.environ.get('CONTENT_LENGTH', 0))
            except ValueError:
                request_body_size = 0
            request_body = self.environ['wsgi.input'].read(request_body_size)
            self.request_data = parse_qs(request_body)

    def render_to_generator(self):
        for key, value in self.environ.items():
            yield ''.join([key, ' = ', value, '\n']).encode()

    def method_type(self):
        return self.environ['REQUEST_METHOD']

    def is_post(self):
        return request.method_type == 'POST'

    def is_get(self):
        return request.method_type == 'GET'

    def is_put(self):
        return request.method_type == 'PUT'

    def is_delete(self):
        return request.method_type == 'DELETE'




