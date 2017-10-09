import socket


def server_forever(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen()
    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024)
        print(request)

        client_connection.sendall(b"HTTP/1.1 200 OK\n\nHello!")
        client_connection.close()


def handle_request(server_socket, application):
    client_connection, client_address = server_socket.accept()
    raw_request = client_connection.recv(1024)
    response = application(parse_request(raw_request), start_response)
    client_connection.sendall(response)
    client_connection.close()


def run_uwsgi_application(application):
    pass


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello world from a simple WSGI application!']


if __name__ == '__main__':
    server_forever()
