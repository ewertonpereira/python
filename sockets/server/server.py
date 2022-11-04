import socket
from sys import exit

HOST = 'localhost'
PORT = 50000

# TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((HOST, PORT))
except socket.error as err:
    print(f'Bind falhou, código do erro: {err}')
    exit()

server.listen()

# receive conection/address from cliente
conection, address = server.accept()

print('Aguardando conexão de um cliente...')
print(f'Conectado em {address}')

checksum = 0
data = bytearray()

while True:
    data_server = conection.recv(1024)
    index = len(data_server) - 1

    if not data_server:
        conection.close()
        break
    data.extend(data_server)

    for element in data[index:]:
        checksum ^= element

    key = int.from_bytes(data[index:], "big")
    message = data[1:index-1]

    if key == checksum:
        conection.sendall(message)
    else:
        conection.close()
