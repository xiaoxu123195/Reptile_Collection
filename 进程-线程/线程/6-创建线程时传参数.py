import threading
import time


def print_lines(num):
    for i in range(num):
        print('1111')
        time.sleep(0.1)


def print_lines2(num1, num2):
    for i in range(num1):
        print('22222')
        time.sleep(0.1)

    for i in range(num2):
        print('333333')
        time.sleep(0.1)


# args 必须是一个元组 所以形式为 args=(5,)
t1 = threading.Thread(target=print_lines, args=(3,))
t2 = threading.Thread(target=print_lines2, args=(2, 5))
t1.start()
t2.start()

