from framework import Request
from framework import get_404_not_found, debug_message
from framework import Router

def application(environ, start_response):
    rules = {
        '/': 'mymodel_list',
        'mymodel/': 'mymodel_show'
    }
    request = Request(environ)
    router = Router(rules, request)
    controller, model, view, template_path = router.route()
    if isinstance(controller, object) and isinstance(model, object) \
            and isinstance(template_path, str):
        controller.connect('db.sqlite')
        response = debug_message('COOL', start_response)
        print(view)
    else:
        response = get_404_not_found(request, start_response, True)

    return response

