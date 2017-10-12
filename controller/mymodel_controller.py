import sqlite3

class Controller(object):

    def __init__(self):
        self.connection = None

    def connect(self, path_to_db):
        try:
            self.connection = sqlite3.connect(path_to_db)
        except sqlite3.DatabaseError:
            pass

    def processing_request(self, request, model):
        if request.is_get():
            if isinstance(self.connection, object):
                cursor = self.connection.cursor()
                cursor.execute('''
                    Select * From ?
                ''',model.table_name)
        elif request.is_post():
            pass
        elif request.is_put():
            pass
        elif request.is_delete():
            pass
