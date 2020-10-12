import xmlrpc.client as xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000')
print("try to start invoke remote api")
print(proxy.start())
