from urllib.parse import parse_qs


class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.request_data = None
        self._parse_request_data()
        self.parsed = 'no'

    def _parse_request_data(self):
        if self.is_get():
            self.request_data = parse_qs(self.get_query_string())
            self.parsed = 'yes'
        elif self.is_post():
            try:
                request_body_size = int(self.environ.get('CONTENT_LENGTH', 0))
            except ValueError:
                request_body_size = 0
            request_body = self.environ['wsgi.input'].read(request_body_size)
            self.request_data = parse_qs(request_body)

    def get_query_string(self):
        return self.environ['QUERY_STRING']

    def debug_render_to_text(self):
        for key, value in self.environ.items():
            yield ''.join([key, ' = ', str(value), '\n']).encode()

    def debug_render_to_html(self):
        for key, value in self.environ.items():
            yield ''.join(['<b>',key,' = </b>',' ',str(value),'<br>']).encode()

    def get_request_uri(self):
        if self.environ['REQUEST_URI'] != '':
            return self.environ['REQUEST_URI']
        elif self.environ['PATH_INFO'] != '':
            return self.environ['PATH_INFO']
        elif self.environ['QUERY_STRING'] != '':
            return self.environ['QUERY_STRING']
        else:
            return

    def method_type(self):
        return self.environ['REQUEST_METHOD']

    def is_post(self):
        return self.method_type() == 'POST'

    def is_get(self):
        return self.method_type() == 'GET'

    def is_put(self):
        return self.method_type() == 'PUT'

    def is_delete(self):
        return self.method_type() == 'DELETE'

    def is_unsupported_method(self):
        return self.method_type() not in ['POST', 'PUT', 'GET', 'DELETE']
