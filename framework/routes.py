'''
Module contain simple router. URLs in dictionary rules.
rules dictionary - user defined in application.py
'''

import os
import re
import importlib.util


class Router(object):
    def __init__(self, rules, request):
        self.root_path = os.path.abspath('.')
        self.rules = rules
        self.uri = request.get_request_uri()

    def _load_module(self, mod_path, mod_name):
        spec = importlib.util.spec_from_file_location(mod_name, mod_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod


    def route(self):
        controller = None
        model = None
        template_path = None
        view = None
        values = None
        for key, value in self.rules.items():
            if re.match(key, self.uri):
                values = value.split('_')
                break
        if values is not None:
            controller_path = os.path.join(self.root_path, 'controller', values[0] + '_controller.py')
            model_path = os.path.join(self.root_path, 'model', values[0] + '_model.py')
            view_path = os.path.join(self.root_path, 'view', 'views.py')
            template_path = os.path.join(self.root_path, 'template', values[1] + '.html')
            controller = self._load_module(controller_path, 'c').Controller()
            model = self._load_module(model_path, 'm')
            view_module = self._load_module(view_path, 'v')
            view = getattr(view_module, values[1] + '_view')
        return controller, model, view, template_path, values[1]






