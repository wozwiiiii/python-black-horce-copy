#while循环的基础语法
"""演示while循环的基础运用"""

i = 0
while i < 100:
    print("小美，我喜欢你")
    i += 1



#for循环的基础语法
"""演示for循环的基础语法"""
name = "itheima"

for x in name:
    """
    将name的内容，挨个取出赋予x临时变量
    就可以在循环体内对x进行处理
    """
    print(x)



#range语句
"""演示python中range()的基本使用"""

"""range语法1: range(num)
for x in range(10):
    print(x)

range语法2：range(num1,num2)
for x in range(5,10):
#从5开始，到10结束（不含10本身）的一个数字序列，数字之间间隔为1
    print(x)   

range语法3：range(num1,num2,step)
for x in range(5,10,2):
#从5开始，到10结束（不含10本身）的一个数字序列，数字之间间隔为2
    print(x)       
"""

for x in range(10):
    print("我喜欢你，送你一朵玫瑰花")



#变量作用域
"""演示for循环临时变量作用域"""
i = 0
for i in range(5):
    print(i)

print(i)



#循环嵌套使用
"""for循环嵌套"""
i = 0
for j in range(1,11):
    print(f"给小美送的第{j}束花")
print("小美我喜欢你")

print(f"第{i}天，表白成功")


"""while循环嵌套使用"""
#外层：表白100天控制
#内层：每天表白都送10只玫瑰花的控制
i = 1
while i <= 10:
    print(f"今天是第{i}天，准备表白")

    #内层循环控制变量
    j = 1
    while j <= 10:
        print(f"送给小美的第{j}只玫瑰花")
        j += 1
    print("小美我喜欢你")
    i += 1
print(f"坚持到第{i-1}天，表白成功")        



#循环中断
"""中断控制：break和continue"""

import random
num = random.randint(1,10)

"""循环中断语句continue
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")

continue嵌套应用
for i in range(1,6):
    print("语句1")        
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")

循环中断语句 break
for i in range(1,101):
    print("语句1")
    break
    print("语句2")
print("语句3")               
"""

#break嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")


print(num)    