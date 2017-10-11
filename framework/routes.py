import re

rules = {
    'index':'/',
    'page/([-_a-z0-9]+)': 'page/show/1',
    'users/([-_a-z0-9]+)': 'users/show/1'
}

class Router(object):
    def __init__(self, rules, request):
        self.rules = rules
        self.uri = request.get_request_uri()

    def route(self):
        if not self.uri == '/':
            uri_items = self.uri.split('/')
        else:
            pass


