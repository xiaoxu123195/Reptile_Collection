from multiprocessing import Process
import time

MUM = 100


def task1():
    global MUM
    MUM = 200
    print("----------in task1, MUM is %d" % MUM)


def task2():
    print("----------in task2, MUM is %d" % MUM)


p1 = Process(target=task1)
p2 = Process(target=task2)

if __name__ == "__main__":
    p1.start()
    time.sleep(1)
    p2.start()
