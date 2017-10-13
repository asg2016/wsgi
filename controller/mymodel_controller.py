import sqlite3

class Controller(object):

    def __init__(self):
        self.connection = None

    def connect(self, path_to_db):
        try:
            self.connection = sqlite3.connect(path_to_db)
        except sqlite3.DatabaseError:
            pass

    def _fetch_data_to_models(self, data, model):
        model_data = []
        for data_item in data:
            model_instance = model.Model(data_item)
            model_data.append(model_instance)
        return model_data


    def processing_request(self, request, model, cmd):
        if request.is_get():
            if isinstance(self.connection, object):
                data = None
                table_name = model.Model.table_name
                cursor = self.connection.cursor()
                sql = ''
                if request.get_query_string() != '':
                    sql = ''.join([
                        'Select * From ', table_name, ' Where ', request.get_query_string()
                    ])
                elif cmd =='list':
                    sql=''.join(['Select * From ', table_name])
                cursor.execute(sql)
                data = cursor.fetchall()
                return self._fetch_data_to_models(data, model)
            else:
                return
        elif request.is_post():
            pass
