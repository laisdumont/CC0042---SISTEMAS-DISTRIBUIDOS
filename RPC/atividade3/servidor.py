import xmlrpc.server
import socket
import datetime

# Classe que herda de SimpleXMLRPCServer e define as funções remotas
class MeuServidor(xmlrpc.server.SimpleXMLRPCServer):

    def __init__(self, addr, requestHandler=xmlrpc.server.SimpleXMLRPCRequestHandler, logRequests=True, allow_none=True, encoding=None, bind_and_activate=True, use_builtin_types=False):
        super().__init__(addr, requestHandler, logRequests, allow_none, encoding, bind_and_activate, use_builtin_types)
        self.lista = []
        self.register_function(self.armazenar_string)
        self.register_function(self.recuperar_lista)
        self.register_function(self.retornar_ip)
        self.register_function(self.retornar_data_hora)

    # Função remota para armazenar uma string na lista
    def armazenar_string(self, s):
        # Adicionar a string na lista
        self.lista.append(s)
        # Retornar uma mensagem de confirmação
        return f"A string '{s}' foi armazenada na lista."

    # Função remota para recuperar a lista de mensagens
    def recuperar_lista(self):
        # Retornar a lista
        return self.lista

    # Função remota para retornar o IP do servidor
    def retornar_ip(self):
        # Obter o nome do host da máquina que executa o servidor
        host = socket.gethostname()
        # Obter o endereço IP do host
        ip = socket.gethostbyname(host)
        # Retornar o IP
        return ip

    # Função remota para retornar a data e hora do servidor no formato YYYY-MM-DD HH:MM
    def retornar_data_hora(self):
        # Obter a data e hora atual do servidor
        agora = datetime.datetime.now()
        # Formatar a data e hora no formato desejado
        formato = "%Y-%m-%d %H:%M"
        data_hora = agora.strftime(formato)
        # Retornar a data e hora
        return data_hora

# Criar uma instância da classe MeuServidor e passar o endereço e a porta que o servidor deve escutar
servidor = MeuServidor(("", 5000))
# Iniciar o servidor e esperar por conexões dos clientes
servidor.serve_forever()