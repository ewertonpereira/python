import socket
import hashlib


# with open(name_file, 'rb') as file:
#     for data in file.readlines():
#         connection.send(data)


HOST = 'localhost'
PORT = 50000

# conexões - IPV4 ou dominio
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # protocolo tcp
server.bind((HOST, 50000))
server.listen(1)
print('Aguardando conexão de um cliente')

# conexão/endereço cliente
conn, ender = server.accept()

print(f'Conectido em em {ender}')

while True:
    hasher = hashlib.md5()
    # tamanho de dados em bytes - bytes -> string
    data = conn.recv(1024)
    hasher.update(data)
    
    crip = hasher.hexdigest()
    print(crip)
    

    print(data.decode())
    if not data:
        print('Fechando conexão')
        conn.close()
        break
    conn.sendall(data)