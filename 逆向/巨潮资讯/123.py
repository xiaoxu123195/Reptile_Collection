import math
import time
import base64

# 123.js运行结果 10位
# 1658912049
# MTY1ODkxMjA0OQ==

# time1 = math.floor(time.time() * 1000)  运行结果   所以不是每个地方都要乘1000
# 1658912100351
# MTY1ODkxMjEwMDM1MQ==

time1 = math.floor(time.time())
print(time1)
mcode = base64.b64encode(str(time1).encode()).decode()
print(mcode)
