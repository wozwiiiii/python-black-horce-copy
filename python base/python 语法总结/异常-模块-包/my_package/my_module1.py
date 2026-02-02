#__all__ = ['test_a']
#import *时a,b两方法都会导入，但有了这条语句只能调用test_a函数，test_b函数无法使用，但还是可以手动导入


def test_a(x,y):
    result = x + y
    print(f"a的显示结果result:{x}+{y} = {result}")
    print(x + y)


def test_b(x,y):
    result = x - y
    print(f"b的显示result:{x}-{y} = {result}")
    return result


def info_print1():
    print("info_print1方法输出")

#在想引用的目标文件中测试函数方法，不会影响其他文件调用函数(直接出返回值)
if __name__ == '__main__':
   print(test_a(1,2)) 