import threading
import time


class Task(threading.Thread):
    def run(self):
        while True:
            print('1111')
            time.sleep(1)


t = Task()
t.start()

while True:
    print('main')
    time.sleep(1)
