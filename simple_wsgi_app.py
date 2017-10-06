import os
from functools import update_wrapper


def setupmethod(f):
    def wrapper_func(self, *args, **kwargs):
        if self.debug and self._got_first_request:
            raise AssertionError('A setup function was called after the '
                'first request was handled.  This usually indicates a bug '
                'in the application where a module was not imported '
                'and decorators or other functionality was called too late.\n'
                'To fix this make sure to import all your view modules, '
                'database models and everything related at a central place '
                'before the application starts serving requests.')
        return f(self, *args, **kwargs)
    return update_wrapper(wrapper_func, f)


class App(object):
    def __init__(self, debug=True):
        self.debug = debug
        self._got_first_request = True


    def __call__(self, environ, start):
        start('200 OK', [('Content-Type', 'text/plain')])
        self.environ = environ
        return self.print_environ()

    def print_environ(self):
        for key, value in self.environ.items():
            yield ''.join([key, ' ', str(value), '\n']).encode()


app = App()
