from http import client
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM ) # protocolo tcp

client.connect(('localhost', 7777))
print('Conectado')

namefile = str(input('Arquivo>'))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{namefile} recebido"\n')