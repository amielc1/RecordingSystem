import xmlrpc.client as xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000')
proxy.stop()
# print(proxy.start())
