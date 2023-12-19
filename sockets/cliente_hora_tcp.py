import socket
import threading


# TCP
def receber_mensagens(sock):
    data = sock.recv(2048)
    #Imprimindo a mensagem recebida
    print(data.decode())
    sock.sendall("0".encode('utf-8'))
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server_address = ('localhost', 20003)
print ("Conectando %s porta %s" % server_address)
#Conectando ao servidor
sock.connect(server_address)
recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
recepcao.start()
message = "Horas de agora: "
#Enviando mensagem ao servidor
sock.sendall(message.encode('utf-8'))

recepcao.join()