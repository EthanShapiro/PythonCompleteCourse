import socket
import sys

HOSTNAME = ""   # '' means 'localhost' or '127.0.0.1' to only allow connections from this server
PORT = 1234     # Arbitrary port


def Main():
    # try to create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket creation failed with error %s' % err)

    # try to bind to a socket
    try:
        s.bind((HOSTNAME, PORT))
    except socket.gaierror as err:
        print('Bind failed, error code: ' + str(err.args[0]) + '\nMessage: ' + err.args[1])
        sys.exit()

    # start listening to up to 5 clients
    s.listen(5)
    print("Started Listening")

    # Forever loop until we interrupt or
    # an error occurs
    while 1:
        # wait to accept connection
        c, addr = s.accept()
        print("Got a connection from", addr)
        f = open("testfile.txt", 'rb+')
        c.sendfile(f)


if __name__ == "__main__":
    Main()
