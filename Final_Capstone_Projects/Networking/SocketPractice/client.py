import socket

# Create a socket
s = socket.socket()

# Define the port you want to connect to
PORT = 1234

# Connect to the server on local computer
s.connect(('127.0.0.1', PORT))

# Receive data from the server
print(s.recv(1024))
# close the connection
s.close()
