import threading
import time

# 1.定义一个全局变量
g_num = 0


# 2.定义两个函数，用他们来充当线程要执行的代码
def task1():
    global g_num
    g_num = 100
    print("在task1中， g_num=%d" % g_num)


def task2():
    print("在task2中， g_num=%d" % g_num)


# 3.创建线程对象
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# 4.调用start创建线程，让线程开始运行
t1.start()
time.sleep(2)
t2.start()
