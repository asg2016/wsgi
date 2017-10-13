def list_view(list_of_model, start_response):
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Language', 'ru'),
        ('charset', 'utf-8')
    ])
    res = '<head> <meta charset="utf-8"></head>'
    for model in list_of_model:
        res = res.join(['<p><h3>', model.head, ' ', str(model.date), '</h3></p>'])
    return res.encode()

def show_view(model, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ''.join('<h1>', model.head, '</h1>', '<br>', str(model.date), model.text)