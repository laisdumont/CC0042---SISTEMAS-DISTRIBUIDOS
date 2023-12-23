# cliente_rpc.py
from xmlrpc.client import ServerProxy

# Conecta-se ao servidor local
local_server = ServerProxy('http://localhost:8000/RPC2')

# Conecta-se a um servidor remoto
# Substitua 'http://remote-server:8000' pela URL do servidor remoto
remote_server = ServerProxy('http://remote-server:8000/RPC2')

# Testa as funções do servidor local
print("Servidor Local:")
print("Data e Hora Atual:", local_server.get_current_datetime())
print("Quantidade de Chamadas:", local_server.get_call_count())

# Testa as funções do servidor remoto
print("\nServidor Remoto:")
print("Data e Hora Atual:", remote_server.get_current_datetime())
print("Quantidade de Chamadas:", remote_server.get_call_count())
