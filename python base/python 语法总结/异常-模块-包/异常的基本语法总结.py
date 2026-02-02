#异常的出现
#通过open.读取一个不存在的文件
f= open("D:/abc.txt","r",encoding="UTF-8")

#异常的捕获
"""
基本捕获语法
try:
    f = open("D:/abc.txt","r",encoding="UTF-8")
except:
    print(f"出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
    f = open("D:/abc.txt","w",encoding="UTF-8")

捕获指定异常
try:
    print(name)
    #1 / 0
except NameError as e:
    print("出现了未定义变量的异常")
    print(e)

捕获多个异常
try:
    #1 / 0
    print(name)
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义 或者 除以0的异常错误")   
#未正确设置捕获异常类型，将无法捕获异常                        
"""

#捕获所有异常
try:
    f = open("D:/123.txt","r",encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    f = open("D:/123.txt","w",encoding="UTF-8")
else:
    print("很开心，没有异常！")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()



#异常的传递性

#定义一个出现异常的方法
def func1():
    print("func1 开始执行")
    num = 1 / 0  #除以0的异常
    print("func1 结束执行")

#定义一个无异常的方法，调用上述方法
def func2():
    print("func2 开始执行")    
    func1()
    print("func2 结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常信息是：{e}")    

main()


