import socket   # Import socket because we need it
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created!")
except socket.error as err:
    print('socket creation failed with error %s' %(err))

# '' is a symbolic name meaning all available interfaces (Any address can connect)
HOST = ''       # Use 'localhost' or '127.0.0.1' to only allow connections from the computer
PORT = 1234     # Arbitrary non-privileged port

# Try to bind socket to an ip and a port
try:
    s.bind((HOST, PORT))
    print("Socket bind successful")
except socket.error as err:
    print('Bind failed, error code : ' + str(err[0]) + ' Message ' + err[1])
    sys.exit()

# Listen to up to five clients
s.listen(5)
print('Started listening')

# Forever loop until we interrupt or
# an error occurs
while 1:
    # wait to accept connection
    c, addr = s.accept()
    print("Got a connection from", addr)

    # Send data to client
    c.send(b'Thank you for connecting') 
    # Close connection with client
    c.close()
