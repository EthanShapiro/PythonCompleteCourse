import socket

HOSTNAME = "127.0.0.1"
PORT = 5001

SERVER = ("127.0.0.1", 5000)

def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOSTNAME, PORT))

    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode("utf-8"), SERVER)
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        print("Recieved from server: " + data)
        message = input("-> ")
    s.close()

if __name__ == "__main__":
    Main()