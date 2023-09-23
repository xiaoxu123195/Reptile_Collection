from multiprocessing import Process
import time
# 多进程创建线程跟多线程很类似


def test():
    """子进程单独执行代码"""
    while True:
        print('---test---')
        time.sleep(1)


if __name__ == "__main__":
    p = Process(target=test)
    p.start()

    # 主进程单独执行的代码
    while True:
        print('---main---')
        time.sleep(1)




