import gevent


def f1(n):
    for i in range(n):
        print("-----f1-----", i)


def f2(n):
    for i in range(n):
        print("-----f2-----", i)


def f3(n):
    for i in range(n):
        print("-----f3-----", i)


g1 = gevent.spawn(f1, 5)
g2 = gevent.spawn(f2, 5)
g3 = gevent.spawn(f3, 5)
g1.join()  # join会等待g1标识的那个任务执行完毕之后 对其进行清理工作，其实这就是一个 耗时操作
g2.join()
g3.join()
