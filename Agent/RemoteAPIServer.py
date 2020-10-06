from xmlrpc.server import SimpleXMLRPCServer


class RemoteAPIServer:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = SimpleXMLRPCServer((self.ip, self.port), allow_none=True)

    def register_function(self, func):
        self.server.register_function(func)

    def start_listen(self):
        self.server.serve_forever()
