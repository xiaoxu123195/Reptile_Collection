import threading
import time


def task_1():
    while True:
        print('111111')
        time.sleep(1)


t_1 = threading.Thread(target=task_1)
t_1.start()

while True:
    print('222222')
    time.sleep(1)
