# servidor_rpc.py
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import datetime

# Restringe as operações permitidas no servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Implementa as funções do servidor
class RPCServer:
    def __init__(self):
        self.call_count = 0

    def get_current_datetime(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def get_call_count(self):
        self.call_count += 1
        return self.call_count

# Configura e inicia o servidor
if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler)
    server.register_introspection_functions()
    
    rpc_server = RPCServer()
    server.register_instance(rpc_server)

    print("Servidor RPC iniciado. Aguardando chamadas...")
    server.serve_forever()
