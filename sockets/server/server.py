import socket


# with open(name_file, 'rb') as file:
#     for data in file.readlines():
#         connection.send(data)


#     print('Arquivo enviado!')

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
    # tamanho de dados em bytes - bytes -> string
    data = conn.recv(1024)
    if not data:
        print('Fechando conexão')
        conn.close()
        break
    conn.sendall(data)