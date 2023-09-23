from multiprocessing import Process
import time
# 多进程创建线程跟多线程很类似


class MyProcess(Process):
    def run(self):
        """子进程单独执行代码"""
        while True:
            print('---test---')
            time.sleep(1)


if __name__ == "__main__":
    p = MyProcess()
    p.start()

    # 主进程单独执行的代码
    while True:
        print('---main---')
        time.sleep(1)




