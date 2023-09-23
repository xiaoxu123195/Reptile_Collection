from multiprocessing import Queue

# 初始化一个Queue对象，最多可以接收三条put消息
q = Queue(6)
q.put('111')
q.put('222')
print(q.full())  # False
q.put('333')
print(q.full())  # True

# 因为消息队列已满，所以会导致下面的try都会抛出异常
# 第一个try会等待两秒后再抛出异常
# 第二个try会立即执行抛出异常
try:
    q.put('444', timeout=2)
except:
    print('消息队列已满，现有消息数量:%s' % q.qsize())

try:
    q.put_nowait('555')
except:
    print('1消息队列已满，现有消息数量:%s' % q.qsize())

# 推荐的方式，先判断消息队列是否已满，再写入
if not q.full():
    q.put_nowait('666')

# 读取消息时，先判断消息队列是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
