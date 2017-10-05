
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    print(environ['PATH_INFO'])
    print(environ['REQUEST_URI'])
    print(environ['REQUEST_METHOD'])
    print(environ)
    return [b'Hello world from a simple WSGI application!']