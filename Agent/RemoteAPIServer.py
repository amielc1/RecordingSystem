import logging
from xmlrpc.server import SimpleXMLRPCServer


class RemoteAPIServer:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = SimpleXMLRPCServer((self.ip, self.port), allow_none=True)

    def register_function(self, func):
        logging.debug(f"register_function {func} to SimpleXMLRPCServer")
        self.server.register_function(func)

    def start_listen(self):
        logging.debug("SimpleXMLRPCServer start_listen")
        self.server.serve_forever()
