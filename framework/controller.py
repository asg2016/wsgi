class Controller():

    def __init__(self, request):
        self.request = request

    def processing_request(self):
        if self.request.is_get():
            self._do_get()

