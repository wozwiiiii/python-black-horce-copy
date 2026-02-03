#python中的字面量
#整数型字面量
666
#浮点数字面量
13.14
#字符串型字面量
"努力的小陈"

#通过print语句输出各类字面量
print(666)
print(13.14)
print("努力的小陈")

#注释
#单行注释
"""
多行注释
"""



"""
演示python中变量相关操作
"""
#定义一个变量
money = 50
#通过print语句，输出变量记录的内容
print("钱包还有：",money)

#买了一两个冰淇淋，花费10元
money = money - 20
print("买了冰淇淋花费10元，还剩余：",money,"元")

#假设，每隔一小时，输出一下钱包余额
print("现在是下午一点，钱包余额剩余：",money)
print("现在是下午二点，钱包余额剩余：",money)
print("现在是下午三点，钱包余额剩余：",money)
print("现在是下午四点，钱包余额剩余：",money)

Name = "张三"
Age = 11

name = "张三"
age  = 11




#python中的数据类型
#方式一：使用print直接输出类型信息
print(type("努力的小陈"))
print(type(666))
print(type(13.14))

#方式二：使用变量存储type()语句结果
string_type = type("努力的小陈")
int_type = type(666)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)

#方式三：使用type()语句，查看变量中存储的数据类型信息
name = "努力的小陈"
name_type = type(name)
print(name_type)



#python中的标识符
"""
规则一：内容限定，限定使用：中文，英文，数字,下划线，注意不能以数字开头
错误代码示例：1_name = "张三"
1_name ！ = "张三" 
"""

#规则二：大小写敏感
Itheima = "努力的小陈"
itheima = 666
print(Itheima)
print(itheima)

#规则三：不可使用关键字
"""错误示例：使用了关键字：class = 1
使用了关键字：def = 1
"""
Class = 1



#python中的数据类型转换

#将数字类型转换成字符串
num_str = str(11)
print(type(num_str),num_str)

float_str = str(13.14)
print(type(float_str),float_str)

#将字符串转化为数字
num = int("11")
print(type(num),num)

num2 = float("13.14")
print(type(num2),num2)

"""错误示例，想要将字符串转换成数字，必须要求字符串中的内容都是数字
num3 = int("努力的小陈")
print(type(num3),num3)
"""

#整数转浮点数
float_num = float(11)
print(type(float_num),float_num)

#浮点数转整数
int_num = int(13.14)
print(type(int_num),int_num)

#python的字符串拼接

#字符串字面量之间得拼接
print("努力的小陈"+"会得奖")

#字符串字面量和字符串变量的拼接
name = "努力的小陈"
address = "湖南省永州市宁远县"
tel = "18307495701"
print("我是："+ name +",我的地址是："+ address + "我的电话是" + tel)



#python的字符串格式化
name = "努力的小陈"
message = "找朋友来找：%s" % name
print(message)

#通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "python大数据学科，长沙%s期,毕业平均代码行数：%s" % (class_num,avg_salary)
print(message)

name = "中南林业科技大学"
setup_year = 1960
stock_price = 5000
message = "%s,成立于：%d,今天毕业生平均工资为：%f" % (name,setup_year,stock_price)
print(message)

num1 = 11
num2 = 13.145
print("数字11宽度限制5，结果是:%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字13.145宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字13.145不限制宽度，小数精度2，结果是：%2f" % num2)
