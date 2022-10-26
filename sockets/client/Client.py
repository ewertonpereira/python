import socket
import hashlib


# client.send(namefile.encode())

# with open(namefile, 'wb') as file:
#     while 1:
#         data = client.recv(1000000)
#         if not data:
#             break
#         file.write(data)

# print(f'{namefile} recebido"\n')

HOST = 'localhost'
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # DGRAM = UDP

client.connect((HOST, 50000))
print('Conectado')

text = str.encode(input('Digite sua mensagem: '))
client.sendall(text)
hasher = hashlib.md5()

data = client.recv(1024)
hasher.update(text)
crip = hasher.hexdigest()
print(crip)
print(f'Mensagem ecoada: {data.decode()}')
