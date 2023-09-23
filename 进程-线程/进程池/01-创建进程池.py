from multiprocessing import Pool
import random
import time


def worker(num):
    time.sleep(random.randint(1, 5))
    print("num=%d" % num)


if __name__ == "__main__":
    # 3表示进程池中做多有三个进程一起执行
    pool = Pool(3)

    for i in range(10):
        # print('---%d---' % i)
        # 向进程中添加任务
        # 注意：如果添加的任务数量超过了进程池中进程的个数的话，那么就不会接着向进程池中添加
        # 如果还没有执行的话，他会等待前面的进程结束，然后再往进程池中添加新的进程
        pool.apply_async(worker, (i,))

    pool.close()  # 关闭进程池
    pool.join()  # 主进程在这里等待，只有子进程全部结束之后，再会开启主线程
