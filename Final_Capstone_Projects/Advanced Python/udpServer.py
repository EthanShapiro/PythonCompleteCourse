import socket

HOSTNAME = "127.0.0.1"
PORT = 5000

def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOSTNAME, PORT))

    print("Server Started")
    while 1:
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        print("Message from: " + str(addr))
        print("From user: " + data)
        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode("utf-8"), addr)

if __name__ == "__main__":
    Main()
