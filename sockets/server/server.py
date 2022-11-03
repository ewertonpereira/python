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
    if not data_server:
        conection.close()
        break
    
    print(data_server)
    index = len(data_server) -1
    # key = data_server[index:].hex() # 
    key = (data_server[index:].decode())

    print('---')

    

    print(type(key))
    print(key)
    print('---')
    # phase = data_server[:index].hex() # 
    phase = (data_server[:index].decode())
    print(phase)
    print(type(phase))
    for i in phase:
        print(hexlify(i.encode()))
        print(type(i.encode()))
        #array_data.append(result := literal_eval(hex(i.encode())))
        p = i.encode()
        print(type(p.hex()))
        #checksum ^= p.hex()
    print('---')
    print(checksum)
    conection.sendall(phase.encode())
