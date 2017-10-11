import os
from .helpers import make_dirs

root = os.path.abspath('.')

template_dirs = {
    'templates' : os.path.join(root, 'templates'),
}

make_dirs(template_dirs)

controller_dirs = {
    'controllers': os.path.join(root, 'controllers')
}

make_dirs(controller_dirs)

static_dirs = {
    'static': os.path.join(root, 'static')
}

make_dirs(static_dirs)

file_dirs = {
    'inbox': os.path.join(root, 'inbox')
}

make_dirs(file_dirs)
