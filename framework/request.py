from urllib.parse import parse_qs


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

    def debug_render_to_text(self):
        for key, value in self.environ.items():
            yield ''.join([key, ' = ', value, '\n']).encode()

    def debug_render_to_html(self):
        html = []
        for key, value in self.environ.items():
            html += ['<b>',key,'</b>',' ',value,'<br>']
        return html

    def method_type(self):
        return self.environ['REQUEST_METHOD']

    def is_head(self):
        return self.method_type() == 'HEAD'

    def is_post(self):
        return self.method_type() == 'POST'

    def is_get(self):
        return self.method_type == 'GET'

    def is_put(self):
        return self.method_type == 'PUT'

    def is_delete(self):
        return self.method_type == 'DELETE'

    def is_unsupported_method(self):
        return self.method_type() not in ['HEAD', 'POST', 'PUT', 'GET', 'DELETE']
