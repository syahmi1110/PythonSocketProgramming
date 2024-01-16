import socket
import math

# SERVER SOCKET DEFINE FUNCTION
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# BIND SOCKET TO THE SERVER ADDRESS AND PORT NUMBER
server_socket.bind(('192.168.37.128', 8080))

# LISTENING TO THE CONNECTION
server_socket.listen(5)

print('Server is ready to connect with.')

while True:
    # INCOMING SOCKET ACCEPTION
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}')

    # RADIUS VALUE GET FROM CLIENT
    radius = client_socket.recv(1024).decode()
    radius = float(radius)

    # CALCULATION FUNCTION FOR VOLUME
    volume = (4/3) * math.pi * radius**3

    # SEND VOLUME AFTER CALC INTO CLIENT
    volume = str(volume)
    client_socket.send(volume.encode())

    # SOCKET CLOSE
    client_socket.close()

