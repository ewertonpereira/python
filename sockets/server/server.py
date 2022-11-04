from ast import literal_eval
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
array_data = bytearray()

while True:
    data_server = conection.recv(1024)
    index = len(data_server) - 1

    if not data_server:
        conection.close()
        break
    for i in data_server:
        array_data.append(literal_eval(hex(i)))

    for i in array_data[index:]:
        checksum ^= i

   
    key = int.from_bytes(array_data[index:], "big")
    #print(key)
    
    data = array_data[1:index-1]
   

    if key == checksum:
        conection.sendall(data)
    else:
        conection.close()
