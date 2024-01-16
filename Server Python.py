import socket
import math

# Define the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('192.168.37.128', 8080))

# Start listening for incoming connections
server_socket.listen(5)

print('Server is ready to connect with.')

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}')

    # Receive radius value from client
    radius = client_socket.recv(1024).decode()
    radius = float(radius)

    # Calculate sphere volume
    volume = (4/3) * math.pi * radius**3

    # Send sphere volume back to client
    volume = str(volume)
    client_socket.send(volume.encode())

    # Close the client socket
    client_socket.close()
