import socket
from ast import literal_eval

# T
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 50000

client.connect((HOST, PORT))
print('Conectado')


data_client = str.encode(input('Digite sua mensagem: '))
new_data_client = ''
checksum = 0
array_data = bytearray()


for i in data_client:
    if not array_data:
        array_data.append(result := literal_eval(hex(2)))
    
    checksum ^= literal_eval(hex(i))
    array_data.append(result := literal_eval(hex(i)))
    new_data_client += hex(i)
    print(hex(i), '\n')


array_data.append(result := literal_eval(hex(3)))
array_data.append(checksum)

data = array_data
client.sendall(data)


data_client_received = client.recv(1024)
print(f'Mensagem ecoada: {data_client_received.decode()}')
