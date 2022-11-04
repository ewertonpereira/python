import socket


HOST = 'localhost'
PORT = 50000

# TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))
server.listen()
print('Aguardando conexão de um cliente...')

# receive conection/address from cliente
conection, address = server.accept()

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

    for i in data[index:]:
        checksum ^= i

    key = int.from_bytes(data[index:], "big")
    message = data[1:index-1]

    if key == checksum:
        conection.sendall(message)
    else:
        conection.close()
