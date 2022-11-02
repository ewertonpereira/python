from email.headerregistry import Address
import socket


HOST = 'localhost'
PORT = 50000

# protocolo TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()
print('Aguardando conexão de um cliente...')

# conexão/endereço cliente
conection, address = server.accept()

print(f'Conectado em em {address}')

while True:
    data = conection.recv(1024)
    if not data:
        conection.close()
        break
    conection.sendall(data)
