# 数字优先级 数值越小越优先
import queue

q = queue.PriorityQueue()
q.put((10, 'Q'))  # 存入字符串
q.put((30, 'Z'))  # 存入整数
q.put((20, 'A'))  # 存入字典

print(q.get())
print(q.get())
print(q.get())
