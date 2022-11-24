from contextlib import contextmanager


@contextmanager
def connect(server_name, port):
    print("Connecting to " + server_name + ":" + port)
    yield "conexiunea"
    print("Closing connection to " + server_name)

class Connect:
    def __init__(self, server_name, port):
        self.server_name = server_name
        self.port = port

    def __enter__(self):
        print("connecting to " + self.server_name)
        return "conexiune la " + self.server_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing connection " + self.server_name)


with connect("www.google.com", "80") as connection_:
    print(connection_)