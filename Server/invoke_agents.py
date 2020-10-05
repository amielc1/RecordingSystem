import xmlrpc.client as xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000')
print(proxy.start())
