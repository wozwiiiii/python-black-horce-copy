#演示对于文件的读取

#打开文件
import time

f= open("D:/测试.text","r",encoding="UTF-8")
print(type(f))
"""
读取文件 - read()
print(f"读取10个字节的结果：{f.read(10)}")
print(f"read读取全部内容的结果是：{f.read()}")
"""
print("-----------------------------------")

"""读取文件 - readLines()
lines = f.readlines() #读取文件全部行，封
print(f"lines对象类型是：{type(lines)}")
print(f"lines对象内容是：{lines}")


读取文件 - readline()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")



for循环读取文件行
for line in f:
    print(f"每一行的数据是：{line}")

f.close()  #文件关闭
time.sleep(5000)   
"""

#witlh open 语法操作文件
with open("D:/测试.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

time.sleep(50000)


