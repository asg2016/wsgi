


class Controller():

    def __init__(self, environ):
        self.environ = environ

    def processing_request(self):
        pass


    def is_get(self):
        return self.environ['REQUEST_METHOD'] == 'GET'


    def is_post(self):
        return self.environ['REQUEST_METHOD'] == 'POST'


    def is_put(self):
        return self.environ['REQUEST_METHOD'] == 'PUT'


    def is_delete(self):
        return self.environ['REQUEST_METHOD'] == 'DELETE'
