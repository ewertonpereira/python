import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # DGRAM = UDP

HOST = 'localhost'
PORT = 50000

client.connect((HOST, PORT))
print('Conectado')


client.sendall(str.encode(input('Digite sua mensagem: ')))


data = client.recv(1024)
print(f'Mensagem ecoada: {data.decode()}')
