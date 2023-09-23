from greenlet import greenlet
import time


def test1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("---B--")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

# 切换到gr1中运行
gr1.switch()

# 协程与进程、线程的不同
# 1. 进程、线程 创建完之后，到底是哪个进程、线程执行 不确定，这要让操作系统来进行计算（调度算法，例如优先级调度）
# 2. 协程是可以人为来控制的
