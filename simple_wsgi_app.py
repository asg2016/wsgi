#
# def app_start(environ, start_response):
#     pass
#
# class Request(object):
#     def __init__(self,environ):
#         self.method =


# код рабочий но возможно класс избыточен
class App(object):
    def __init__(self, debug=True):
        self.debug = debug


    def __call__(self, environ, start):
        start('200 OK', [('Content-Type', 'text/plain')])
        self.environ = environ
        return self.print_environ()

    def print_environ(self):
        for key, value in self.environ.items():
            yield ''.join([key, ' ', str(value), '\n']).encode()


app = App()
