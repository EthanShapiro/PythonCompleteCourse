import threading
import time


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        super().__init__()
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, 'a') as f:
            f.write(self.text+"\n")
        time.sleep(2)
        print("Finished Background File Write to " + self.out)

def Main():
    message = input("Enter a string to store")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("The program can continue while it writes in another thread")
    print("100 + 400 = 500")

    background.join()
    print("Waited for thread to finish")

if __name__ == "__main__":
    Main()
