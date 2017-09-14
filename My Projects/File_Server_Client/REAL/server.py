import socket

HOST = ""
PORT = 5001


def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to an address and port
    s.bind((HOST, PORT))

    # Listen to up to 1 connection
    s.listen(1)

    while 1:
        print("Waiting for connection")
        c, addr = s.accept()
        print("Connected to " + str(addr))
        f = open("1MB.txt", "rb+")
        b1 = f.read()
        c.sendall(b1)
        f.close()
        print("received request")
        break


Main()

