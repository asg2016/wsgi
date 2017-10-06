import os
import datetime

def make_dirs(dirs_dict):
    for key, value in dirs_dict.items():
        if not os.path.exists(value):
            os.makedirs(value)


def get_404_not_found(request, start_response, debug=True):
    debug_msg = None
    if debug:
        debug_msg = request.debug_render_to_html()
    return start_response('404 Not Found',
                          [
                              ('Content-Type', 'text/html'),
                              ('Server', request.environ['SERVER_NAME']),
                              ('Date', '{}'.format(datetime.datetime.now())),
                              ('Content-Language', 'ru')
                          ]), debug_msg