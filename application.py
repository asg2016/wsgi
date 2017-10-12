from framework import Request
from framework import get_404_not_found
from framework import Router

def application(environ, start_response):
    rules = {
        '/': 'mymodel_list',
        'mymodel/': 'mymodel_show'
    }
    request = Request(environ)
    router = Router(rules, request)
    controller, model, template_path = router.route()
    if isinstance(controller) and isinstance(model) \
            and isinstance(template_path):
        print(controller)
    else:
        response = get_404_not_found(request, start_response, True)
    return response
