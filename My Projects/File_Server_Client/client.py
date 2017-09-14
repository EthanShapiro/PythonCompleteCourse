import socket

HOSTNAME = "127.0.0.1"   # '' means 'localhost' or '127.0.0.1' to only allow connections from this server
PORT = 5001     # Arbitrary port


def Main():
    # try to create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket creation failed with error %s' % err)

    recv_buff = bytearray(1024)
    recv_view = memoryview(recv_buff)
    size = 0
    data = []

    s.connect((HOSTNAME, PORT))
    while True:
        d = s.recv(1024)
        if not d:
            break
        data.append(d)

    with open("testsave.txt", "wb") as f:
        f.writelines(data)
    print("Wrote to file")

    s.close()


if __name__ == "__main__":
    Main()

