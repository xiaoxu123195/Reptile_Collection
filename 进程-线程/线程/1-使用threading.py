from time import sleep
import threading


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)


if __name__ == "__main__":
    # 共需6s
    # sing()
    # dance()
    # 3s
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
