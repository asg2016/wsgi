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
            and isinstance(template_path, str):
        controller.connect('db.sqlite')
        debug_message('', start_response)
        response = request.debug_render_to_text()
        print(request.request_data)
        print(request.method_type())
        print(request.get_query_string())
        print(request.is_get())
    else:
        response = get_404_not_found(request, start_response, True)

    return response

