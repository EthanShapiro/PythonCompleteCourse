import socket

HOSTNAME = "127.0.0.1"
PORT = 5000

def Main():
    s = socket.socket()
    s.connect((HOSTNAME, PORT))

    message = input("-> ")
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Recieved from server: " + data)
        message = input("-> ")
    s.close()

if __name__ == "__main__":
    Main()
