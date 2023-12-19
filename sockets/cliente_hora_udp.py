import socket
import threading

# UDP
server_address = ('localhost', 20003)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ("Enviando para %s porta %s" % server_address)

sock.sendto(''.encode('utf-8'), server_address)

message, address = sock.recvfrom(2048)
print('Horas de agora: ' + message.decode())

sock.close()