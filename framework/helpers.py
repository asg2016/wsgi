import os
import traceback
import datetime

def make_dirs(dirs_dict):
    for key, value in dirs_dict.items():
        if not os.path.exists(value):
            os.makedirs(value)


def traceback_to_browser(start_response):
    start_response('500 Internal Error',[('Content-Type', 'text/plain')])
    return traceback.format_exc()


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