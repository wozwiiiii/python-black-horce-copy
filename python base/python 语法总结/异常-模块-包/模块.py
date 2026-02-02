"""
演示Python的模块导入
"""

from time import sleep


# 使用import导入time模块使用sleep功能（函数）
# import time     # 导入Python内置的time模块（time.py这个代码文件）
# print("你好")
# time.sleep(5)   # 通过. 就可以使用模块内部的全部功能（类、函数、变量）
# print("我好")

# 使用from导入time的sleep功能（函数）
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")

# 使用 * 导入time模块的全部功能
# from time import *      # *表示全部的意思
# print("你好")
# sleep(5)
# print("我好")

# 使用as给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

from time import sleep as sl
print("你好")
sl(5)
print("我好")



#演示自定义模块
"""
导入自定义模块使用
import my_module1
from my_module1 import test
test(1,2)

导入不同模块的同名功能
from my_module1 import text
from my_module2 import text
test(1,2) #后面的会覆盖掉前面方法产生的值
__main__变量
from my_module1 import test
"""


from my_package import my_module1
result = my_module1.test_a(1,2)
print(f"结果是：{result}")


"""
演示常用的模块功能
"""
import time
# time模块
ts = time.time()        # 当前时间戳
print(f"当前时间戳是：{ts}")

# 获取当前时间以指定的格式显示,2000-01-01 10:00:00
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 将指定的时间戳转换为格式化的日期字符串
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# random模块

# os模块

# sys模块
