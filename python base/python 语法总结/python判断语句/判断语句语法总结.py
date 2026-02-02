#布尔类型和比较运算符
"""
演示布尔类型的定义
以及比较运算符的应用
"""
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}, 类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}, 类型是：{type(bool_2)}")

""" 
比较运算符的使用
 == , !=, >, <, >=, <=
演示进行内容的相等比较
"""
num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10！=15的结果是{num1 != num2}")

name1 = "itcast"
name2 = "zhongnanlin"
print(f"itccast == zhongnanlin的结果是:{name1 == name2}")

#演示大于小于，大于小于等于的比较运算
num1 = 10
num2 = 3
print(f"10 > 3 的结果是{num1 > num2}")
print(f"10 < 3 的结果是{num1 < num2}")

num1 = 10
num2 = 11
print(f"10 >= 11的结果是：{num1 >= num2}")
print(f"10 <= 11的结果是：{num1 <= num2}")


#if判断语句的基本格式
"""
演示python判断语句：if语句的基本格式应用
"""

age = 10
if age >= 10:
    print("我已经成年了")
    print("即将步入大学生活")
print("时间过得真快呀")    



#if else语句的使用
"""
演示python中
if else的组合判断语句
"""
age = int(input("请输入你的年龄："))

if age >= 18 :
    print("您已成年，需要买票，支付10元。")
else:
    print("您为未成年，可以免费")



#if_elif_else语句的使用
"""
演示python中if elif else的组合判断语句
"""

#通过if判断，可以使用多条件判断的语法
#第一个条件就是if
if int(input("请输入你的身高(cm):")) < 120:
    print("身高小于120cm,可以免票")
elif int(input("请输入您的VIP等级（1-5）：")) > 3:
    print("vip等级大于3，可以免费进入。")
elif int(input("请告诉我今天是几号：")) == 1:
    print("今天是1号，可以免费进入")
else:
    print("不好意思，所有条件都不满足，需要买票，支付10元")




#判断语句的嵌套
"""
演示判断语句的嵌套使用
上述代码可改为
 if int(input("你的身高是多少：")) > 120:
     print("身高超出限制，不可以免费")
     print("但是，如果vip级别大于3，可以免费")

     if int(input("你的vip级别是多少：")) > 3:
         print("恭喜你，vip级别达标，可以免费")
     else:
         print("Sorry 你需要买票10元")
else:
     print("欢迎小朋友，免费游玩。")
"""
#嵌套示例
age = 11
year = 1
level = 1
if age >=18:
    print("你的年龄达标了")
    if year > 2:
        print("恭喜你，年龄和入职时间都达标，可以领取奖励")
    elif level > 3:
        print("恭喜你，年龄和级别达标，可以领取奖励")
    else:
        print("不好意思，尽管年龄达标，但是入职时间和级别都不达标")
else:
    print("年龄太大了")
    



#练习题1：判断是否是成年人
#年龄数据获取，input()
age1 = int(input("请输入你的年龄："))
if age1 >= 18:
    print("你的年龄符合要求")
else:
    print("你的年龄不符合要求，请离开")


#练习题2：依据身高判断是否需要买票
height = int(input("请输入你的身高（cm)："))
if height <= 120:
    print("您的身高符合要求，可以免费进入")
elif 120 < height <=150:
    print("您的身高在150cm以下，可以半价")
else:
    print("您的身高超过规定，请购买全票")
print("祝您玩得开心")


#练习题3：使用if elif else猜数字
num = 10
guess_num = int(input("请输入您猜的数字"))

if guess_num > num:
    print("抱歉您猜错了，您猜的数字较大")
elif guess_num < num:
    print("很抱歉，您猜错了，猜的数字较小")
else:
    print("恭喜您猜对了")


#优化版猜数字
if int(input("请输入您猜的数字：")) == num:
    print("恭喜您猜对了")
elif int(input("请输入您猜的数字：")) > num:
    print("抱歉您猜的数字大了，还剩一次机会")
elif int(input("请输入您猜的数字：")) < num:
    print("抱歉您猜的数字小了，还剩一次机会")
else:
    print("很抱歉您猜错了，没有机会了")
    

# 最后一题标准示例：通过键盘输入获取猜想的数字，通过多次if 和 elif的组合进行猜想比较
if int(input("请猜一个数字：")) == num:
    print("恭喜第一次就猜对了呢")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry 猜错了")


