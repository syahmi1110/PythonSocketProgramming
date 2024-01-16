import socket

# Define the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('192.168.37.128', 8080))

# Get radius value from user
radius = input('Enter radius value for the sphere volume: ')

# Send radius value to server
client_socket.send(radius.encode())

# Receive sphere volume from server
volume = client_socket.recv(1024).decode()

# Print the received sphere volume
print(f'Sphere volume for radius {radius} is {volume}')

# Close the client socket
client_socket.close()
