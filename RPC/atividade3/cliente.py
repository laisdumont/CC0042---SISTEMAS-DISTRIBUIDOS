import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://localhost:5000")

# Armazenar uma string na lista do servidor
resposta = servidor.armazenar_string("Olá, mundo!")
print(resposta)

# Recuperar a lista de mensagens do servidor
resposta = servidor.recuperar_lista()
print(resposta)

# Retornar o IP do servidor
resposta = servidor.retornar_ip()
print(resposta)

# Retornar a data e hora do servidor no formato YYYY-MM-DD HH:MM
resposta = servidor.retornar_data_hora()
print(resposta)
