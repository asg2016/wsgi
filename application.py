'''
Application module.
The logic of the web application
Application deploy on the uwsgi
dependencies in requirements.txt
'''

from framework import Request
from framework import get_404_not_found, debug_message
from framework import Router

def application(environ, start_response):
    rules = {
        'mymodel/': 'mymodel_show',
        '/': 'mymodel_list'
    }
    request = Request(environ)
    router = Router(rules, request)
    controller, model, view, template_path = router.route()
    if isinstance(controller, object) and isinstance(model, object) \
        and isinstance(template_path, str) and callable(view):
        controller.connect('db.sqlite')
        data = controller.processing_request(request, model,'list')
        debug_message('', start_response)
        response = view(data, start_response)
        print(view)
    else:
        response = get_404_not_found(request, start_response, True)

    return response
