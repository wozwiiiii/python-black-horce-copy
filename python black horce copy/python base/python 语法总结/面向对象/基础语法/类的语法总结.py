"""
面向对象类中的成员方法定义和使用
"""

#定义一个带有成员方法的类
class Student:
    name = None
    
    def say_hi(self):
        print(f"大家好，我是{self.name},希望大家多多关照")


    def say_hi2(self,msg):
        print(f"大家好，我是：{self.name},来自：{msg}")    



stu = Student()        
stu.name = "陈登基"
stu.say_hi2("湖南")


stu2 = Student()
stu2.name = "陈登财"
stu2.say_hi2("永州市")



"""
演示类与对象的关系，即面向对象的编程套路（思想）
"""

#设计一个闹钟类
class Clock:
    id = None  #序列化
    price = None  #价格

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

#构建两个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID:{clock1.id},价格:{clock1.price}")
#clock1.ring()

clock2 = Clock()
clock2.id = "003033" 
clock2.price = 21.99
print(f"闹钟ID:{clock2.id},价格:{clock2.price}")
clock2.ring()



"""
类的构造方法
"""
#使用构造方法对成员变量进行赋值
#构造方法的名称：__init__

class Student2:

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student2类构建了一个类对象")

stu3 = Student2("陈登基", 20, "18307495701")        
print(stu3.name)
print(stu3.age)
print(stu3.tel)


"""
其他内置方法，python内置的各类魔术方法
"""

class Magic:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    #__str__魔术方法
    def __str__(self):
        return f"Magic类对象,name:{self.name},age:{self.age}"    

    #__lt__魔术方法
    def __lt__(self,other):
        return self.age < other.age

    #__le__魔术方法
    def __le__(self,other):
        return self.age <= other.age
    
    #__eq__魔术方法
    def __eq__(self,other):
        return self.age == other.age
    
stu1 = Magic("陈登基",20)    
stu2 = Magic("陈登财",18)
print(stu1 ==stu2)



"""
封装
面向对象封装思想中私有成员的使用
"""

#定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage__ = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage__ >=1:
            print("5g通信已开启")    
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通信，并已设置单核运行进行省电")


phone = Phone()
phone.call_by_5g()




"""
变量的类型注解
"""
#基础数据类型注解
import json
import random

"""
var_1: int = 10
var_2: str = "zhongnanlin"
var_3: bool = True
"""
#类对象类型注解
class Student4:
    pass
stu: Student4 = Student4()

"""
基础容器类型注解
my_list: list = [1,2,3]
my_tuple: tuple = (1,2,3)
my_dict: dict = {"zhongnanlin":444}
"""
#容器类型详细注解
my_list: list[int] = [1,2,3]
my_tuple: tuple[int,str,bool] = (1, "zhongnanlin", True)
my_dict: dict[str,int] = {"zhongnanlin":444}

#在注释中进行类型注解
var_1 = random.randint(1,10) #type: int
var_2 = json.loads('{"name": "zhongnanlin"}') #type: dict[str,str]
def func():
    return 10
var_3 = func() #type: int
"""
类型注解的限制
var_4: int = "zhongnanlin"
var_5: str = 123
"""

"""
对于函数方法进行类型注释
"""

#对形参进行类型注释
def add(x: int,y: int):
    return x + y

#对返回值进行类型注解
def func2(data: list) -> list:
    return data
print(func2(2))

"""
Union联合类型注解
"""
#使用Union类型，必须先导入包
from typing import Union

my_list1: list[Union[int,str]] = [1, 2, "zhongnanlin", "chendengji"]

def func1(data: Union[int,str]) -> Union[int,str]:
    pass




"""
多态
面向对象的多态特性以及抽象类接口的使用
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")    

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    """制造点噪音，需要传入Animal对象"""        
    animal.speak()

#演示多态，使用两个子类对象来调用函数
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


#演示抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()


make_cool(midea_ac)
make_cool(gree_ac)





"""
封装练习题:设计带有私有成员的手机
"""
#设计一个类：描述手机
class myphone:
    #私有成员变量：__is_ing_5g
    __is_ing_5g = True  #5g状态

    #私有成员方法：__check_5g()
    def __check_5g(self):
        if self.__is_ing_5g:
            print("5g正常运行")
        else:
            print("5g无法正常运行，使用4g")

    #提供公开成员方法：call_by_5G()
    def call_by_5G(self):
        self.__check_5g()
        print("正在通信中")

phone = myphone()
phone.call_by_5G()        
            
