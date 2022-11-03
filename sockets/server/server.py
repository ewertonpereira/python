from ast import literal_eval
import socket
from binascii import hexlify


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


checksum = 0
array_data = bytearray()

while True:
    data_server = conection.recv(1024)
    index = len(data_server) - 1

    if not data_server:
        conection.close()
        break
    for i in data_server:
        array_data.append(result := literal_eval(hex(i)))

    for i in array_data[index:]:  
        checksum ^= (i)
        print(checksum)

    print(array_data)
    print(type(array_data))
    index = len(data_server) - 1
    key = array_data[index:]
    print(key)
    phase = array_data[:index]
    print(phase)
    print(f'final: {checksum}')

    '''
  
    for i in phase:
        print(hexlify(i.encode()))
        print(type(i.encode()))
        #array_data.append(result := literal_eval(hex(i.encode())))
        p = i.encode()
        print(type(p.hex()))
        #checksum ^= p.hex()
    print('---')
    print(checksum)'''
    conection.sendall(data_server)
