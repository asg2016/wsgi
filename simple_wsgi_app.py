import os

def run(host, port, app_name):
    pass

def application_run(environ, start_response):
    app = UWSGIApp(environ, start_response)
    return app.get_response()


class Request():
    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD']


class UWSGIApp():
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __call__(self):

    def get_method(self):
        return self.environ['REQUEST_METHOD']

    def get_response(self):
        self.start_response('200 OK', [('Content-Type', 'text/plain')])
        if self.get_method() == 'POST':
            return [b'POST METHOD']
        elif self.get_method() == 'GET':
            return [b'GET METHOD']
        return [b'NOTHING']


if __name__=='__main':
    pass