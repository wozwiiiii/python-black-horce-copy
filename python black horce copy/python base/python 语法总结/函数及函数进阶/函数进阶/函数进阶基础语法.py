#函数多返回值
"""
多返回值示例
"""
#演示使用多个变量，接收多个返回值
def test_return():
    return 1,"hello",True

x,y,z = test_return()
print(x,y,z)



#函数多种使用参数
"""
多种传参形式
"""
#位置参数-默认使用形式
def user_info1(name,age,gender):
    print(f"姓名是{name},年龄是{age},性别是{gender}")

user_info1('Mike',20,'man')


#关键字参数
user_info1(name = 'Anny',age = 18,gender = 'women')
user_info1(age = 23,gender = 'man',name = 'Tommy')
user_info1('小明',gender = 'man',age = 28)


#缺省参数(默认值)
def user_info2(name,age,gender): 
    print(f"姓名是{name},年龄是{age},性别是{gender}")

user_info2('小天',13,'man')


#不定长 - 位置不定长，*号
#不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info3(*args):
    print(f"args参数类型是:{type(args)},内容是{args}")

user_info3(1,2,3,'小明','man')


#不定长 - 关键字不定长，**号
def user_info4(**kwargs):
    print(f"arg参数类型是：{type(kwargs)},内容是：{kwargs}")

user_info4(name = '小明',age = 18,gender = 'man')



#函数作为参数传递
#定义一个函数，接收另外一个函数作为传入函数
def test_func(compute):
    result = compute(1,2) #确定compute是函数
    print(f"compute的参数类型是：{type(compute)}")
    print(f"计算结果：{result}")

#定义一个函数，准备作为参数传入另一个函数
def compute(x,y):
    return x + y    

#调用，并传入函数
test_func(compute)



#lamble匿名函数
test_func(compute)
test_func(lambda x, y : x + y)  #通过lamble匿名函数形式，将其作为参数传入

