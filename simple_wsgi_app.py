import os


# def run(host, port, app_name):
#     pass
#
# def application_run(environ, start_response):
#     app = UWSGIApp(environ, start_response)
#     return app.get_response()
#
#
# class Request():
#     def __init__(self, environ):
#         self.method = environ['REQUEST_METHOD']


class UWSGIApp():
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __call__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield [b'Hello class!!!']

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield [b'Hello class!!!']

    def get_method(self):
        return self.environ['REQUEST_METHOD']

    def get_response(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        if self.get_method() == 'POST':
            return [b'POST METHOD']
        elif self.get_method() == 'GET':
            return [b'GET METHOD']
        return [b'NOTHING']


class App(object):
    def __call__(self, environ, start):
        start('200 OK', [('Content-Type', 'text/plain')])
        self.environ = environ
        return self.print_environ()

    def print_environ(self):
        for key, value in self.environ.items():
            yield ''.join([key, ' ', str(value), '\n']).encode()


app = App()
