import socket


# TCP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 50000

client.connect((HOST, PORT))
print('Conectado\n')

data_client = str.encode(input('Digite sua mensagem: '))
data = bytearray('2', 'utf-8')
checksum = 0

for element in data_client:
    checksum ^= element

data.extend(data_client)
data.extend(bytearray('3', 'utf-8'))
data.append(checksum)

client.sendall(data)

data_client_received = client.recv(1024)
print(f'\nA Mensagem entregue: ({data_client_received.decode()})')
