import sqlite3
from .helpers import traceback_to_browser

class Controller():

    def __init__(self, request, start_response, debug=True):
        self.request = request
        self.err = None
        self.debug = True
        self.start_response = start_response

    def connect(self, db):
        try:
            self.db = sqlite3.connect(db)
        except sqlite3.DatabaseError as self.err:
            traceback_to_browser(self.start_response)


    def processing_request(self):
        pass

