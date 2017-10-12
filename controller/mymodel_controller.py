import sqlite3
from framework.helpers import traceback_to_browser

class Controller(object):

    def __init__(self):
        self.request = None
        self.connection = None

    def connect(self, path_to_db):
        try:
            self.connection = sqlite3.connect(path_to_db)
        except sqlite3.DatabaseError:
            pass

    def processing_request(self, request, model):
        if request.is_get():
            pass
        elif request.is_post():
            pass
        elif request.is_put():
            pass
        elif request.is_delete():
            pass

