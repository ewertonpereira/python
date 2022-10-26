import socket


# conexões - IPV$ ou dominio
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM ) # protocolo tcp

server.bind(('localhost', 7777))
server.listen(1)

# conexão/endereço cliente
connection, address = server.accept()

# tamanho de dados que deseja receber em bytes - bytes -> string
name_file = connection.recv(1024).decode()

with open(name_file, 'rb') as file:
    for data in file.readlines():
        connection.send(data)


    print('Arquivo enviado!')