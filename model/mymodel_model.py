class Model(object):
    table_name = 'mymodel'
    def __init__(self, *args):
        print(args)
        self.id = args[0][0]
        self.head = args[0][1]
        self.text = args[0][2]
        self.date = args[0][3]
