import threading
import time


def say_sorry():
    for i in range(5):
        print("i am sorry")
        time.sleep(1)


t1 = threading.Thread(target=say_sorry)
t2 = threading.Thread(target=say_sorry)
t1.start()
t2.start()



