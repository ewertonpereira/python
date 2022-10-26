import socket


# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM ) # protocolo tcp

# client.connect(('localhost', 7777))
# print('Conectado')

# namefile = str(input('Arquivo>'))

# client.send(namefile.encode())

# with open(namefile, 'wb') as file:
#     while 1:
#         data = client.recv(1000000)
#         if not data:
#             break
#         file.write(data)

# print(f'{namefile} recebido"\n')

HOST = '127.0.0.1'
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # DGRAM = UDP

client.connect((HOST, 50000))
print('Conectado')

client.sendall(str.encode(input('Digite sua mensagem: ')))

data = client.recv(1024)
print(f'Mensagem ecoada: {data.decode()}')
