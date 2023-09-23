from multiprocessing import Process


def task(name, age, **kwargs):
    print('name', name)
    print('age', age)
    print(kwargs)


if __name__ == '__main__':
    p = Process(target=task, args=("xiaohong", 18), kwargs={"mm": 10})
    p.start()
