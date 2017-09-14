import threading
import time

def download_bar(delay):
    download_percent = 0
    while download_percent < 100:
        download_percent += 10
        print("{" + "#"*download_percent + "}" + str(download_percent) + "%")
        time.sleep(delay)

t1 = threading.Thread(target=download_bar, args=[2])
t1.start()
