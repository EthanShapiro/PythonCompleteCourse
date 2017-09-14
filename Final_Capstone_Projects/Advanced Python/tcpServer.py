import socket

HOSTNAME = "127.0.0.1"
PORT = 5000

def Main():
    s = socket.socket()
    s.bind((HOSTNAME, PORT))

    s.listen(2)
    c, addr = s.accept()
    print("Connection from " + str(addr))
    while 1:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        c.send(data.encode('utf-8'))
    c.close()

if __name__ == "__main__":
    Main()
