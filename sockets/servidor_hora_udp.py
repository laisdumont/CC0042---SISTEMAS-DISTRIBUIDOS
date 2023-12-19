import socket
import threading
from datetime import datetime

# UDP
def conexao_cliente(sock, client, address):    
    print('Requisição recebida de %s %s' % address)
    time = datetime.now()
    timeString = time.strftime('%Hh%M')
    sock.sendto(timeString.encode('utf-8'), address)

server_address = ('localhost', 20003)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("Iniciando servidor na porta %s %s\n" % server_address)
sock.bind(server_address)

while(True):
    client, address = sock.recvfrom(2048)
    conexao = threading.Thread(target=conexao_cliente,args=(sock, client, address))
    conexao.start()