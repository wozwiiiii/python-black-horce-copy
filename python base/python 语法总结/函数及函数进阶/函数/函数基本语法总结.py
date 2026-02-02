#函数定义
"""演示函数定义语法"""
#定义一个函数，输出相关信息
def say_hi():
    print("hi,我是来自中南林业科技大学的努力的小陈")

#调用函数
say_hi()


"""函数基础定义练习案例：自动查行程码"""
#定义函数
def check():
    #函数体输出信息
    print("欢迎您来到中南林业科技大学！\n请您展示您72小时的行程码")

#调用函数
check()




#函数参数的使用
"""演示函数使用参数"""
#定义两数相加函数，通过参数接受被计算的两个数字
def add(x,y,z):
    result = x + y + z
    print(f"{x}+{y}+{z}={result}")

#调用函数,传入被计算的数字
add(1,2,3)


"""函数参数案例：自动查询温度及健康码"""
def check_off(num):
    print("欢迎来到中南林业科技大学！请展示您现在的体温：")
    if num >= 37.5:
        print(f"很抱歉您的体温为{num}度未达标，不能进入")
    else:
        print(f"您的体温为{num}度，欢迎您的到来")

#调用函数
check_off(38)        



#返回值定义语法
"""函数返回值语法格式"""
def add2(a,b):
    result = a + b
    #通过返回值，将相加结果返回给调用者
    return result
    print("我完事了")

#函数返回值可通过变量接收
r = add2(5,6)    
print(r)



#特殊字面量：None
#无return语句的函数返回值
def say_hello():
    print("你好呀")

result = say_hello()
print(f"无返回值函数，返回内容是：{result}")    
print(f"无返回值函数，返回内容类型是：{type(result)}")


#主动返回None函数
def say_hello2():
    print("你好呀")
    return None

result = say_hello2()
print(f"无返回值函数，返回内容是：{result}")    
print(f"无返回值函数，返回内容类型是：{type(result)}")


#None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
    
result = check_age(17)
if not result:
    #进入if表示result是None值，即False
    print("未成年，不可进入")    

#None用于声明无初始内容的变量
name = None
print(name,type(name))
print(None)




# 定义函数，进行文档说明
def add3(x, y):
    """
    add函数可以接收2个参数，进行2数相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是2数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是：{result}")
    return result

add3(5, 6)


#函数嵌套使用
#定义函数fun_b
def fun_b():
    print("---2---")
#定义函数fun_a,并在内部调用fun_b
def fun_a():
    print("---1---")

    #嵌套调用
    fun_b()

    print("---3---")

#调用函数fun_a
fun_a()



#变量作用域
"""在函数使用时，定义的变量作用域"""
"""
演示局部变量：
def test_a():
   num = 100
   print(num)

test_a()
出了函数体，局部变量就无法使用
print(num)

演示全局变量:
num = 200
def test_a():
    print(f"test_a:{num}")

def test_b():
    print(f"test_b:{num}")

test_a()
test_b()
print(num)

在函数内修改全局变量：
num = 200
def test_a():
    print(f"test_a:{num}")

def test_b():
    num = 500  局部变量
    print(f"test_b:{num}")

test_a()
test_b()
print(num)
"""

#global关键字，在函数中声明变量为全局变量
num = 200

num = 200
def test_a():
    print(f"test_a:{num}")

def test_b():
    global num
    num = 500  #设置内部定义的变量为全局变量
    print(f"test_b:{num}")

test_a()
test_b()
print(num)    



#函数快速体验
"""需求，统计字符串长度，不使用内置函数len()"""

print("欢迎来到我们的公司！请出示您的健康码及72小时行程码，并配合测量体温")
print("体温测量中，您的体温合格，可以正常进入")



#list列表循环：while和for
def list_while_func():
    """
    使用while循环遍历列表演示函数
    """
    my_list = ["中南大学","湖南大学","中南林业科技大学"]
        #循环控制变量通过下表索引来控制，默认为0
        # 每一次循环将下标索引变量＋1
        # 循环条件：下标索引变量<列表元素数量

    #定义一个变量用来标记列表下标
    index = 0  #初始值为0
    while index < len(my_list):
        #通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表元素：{element}")

        #将循环变量（index）每次循环加1
        index += 1
        

def list_for_func():
    """"
    使用for循环遍历列表演示函数
    ：return:None
    """
    my_list = [1,2, 3, 4, 5]
    #for 临时变量 in 数据容器：
    for element in my_list:
        print(f"列表的元素有：{element}")
        

list_while_func()
list_for_func()