# 先进后出
import queue

q = queue.LifoQueue()
q.put("11")  # 存入字符串
q.put(22)  # 存入整数
q.put({'num': 100})  # 存入字典

print(q.get())
print(q.get())
print(q.get())
