import threading
import time


def task_1():
    while True:
        print('11111')
        time.sleep(1)


def task_2():
    while True:
        print('3333333')
        time.sleep(0.2)


t_1 = threading.Thread(target=task_1)
t_2 = threading.Thread(target=task_2)
t_1.start()
t_2.start()

while True:
    print('222222')
    time.sleep(1)