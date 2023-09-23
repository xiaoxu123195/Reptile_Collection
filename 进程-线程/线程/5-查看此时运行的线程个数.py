import threading
import time
# threading.enumerate()查看当前的线程数
print(threading.enumerate())


def task_1():
    for i in range(5):
        print('11111')
        time.sleep(1)


t1 = threading.Thread(target=task_1)
t1.start()

print(threading.enumerate())

time.sleep(6)
print(threading.enumerate())
