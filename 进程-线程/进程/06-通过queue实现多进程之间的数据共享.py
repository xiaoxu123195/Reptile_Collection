import multiprocessing
import time


def task1(q):
    for i in ["A", "B", "C"]:
        q.put(i)


def task2(q):
    while True:
        time.sleep(0.5)
        if not q.empty():
            value = q.get()
            print("提取的数据是:", value)
        else:
            break


if __name__ == "__main__":
    # 通过Queue实现数据共享
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=task1, args=(q,))
    p2 = multiprocessing.Process(target=task2, args=(q,))

    p1.start()
    p2.start()




