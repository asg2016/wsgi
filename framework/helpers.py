import os
import datetime


def debug_message(msg, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return msg.encode()


def get_404_not_found(request, start_response, debug=True):
    debug_msg = None
    if debug:
        debug_msg = request.debug_render_to_html()
    start_response('404 Not Found',
                          [
                              ('Content-Type', 'text/html'),
                              ('Server', request.environ['SERVER_NAME']),
                              ('Date', '{}'.format(datetime.datetime.now())),
                              ('Content-Language', 'ru')
                          ])
    return debug_msg


def render_template(template_path):
    pass
