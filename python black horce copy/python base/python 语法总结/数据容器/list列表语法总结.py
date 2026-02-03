#list列表
"""
数据容器：list列表
语法：[元素,元素，...]
"""
#定义一个列表
my_list = ["qinghua","beida","python"]
print(my_list,f"其对应类型是{type(my_list)}")

my_list = ["itheima", 666, True]
print(my_list)
print(type(my_list))


#定义一个嵌套列表
my_list = [[1,2,3],[4,5,6]]
print(my_list,f"type = {type(my_list)}")

#通过对应下标索引取出对应位置的数据
my_list = ["xiaochen","liming","xiaohong"]
#列表[下标索引]，从前往后从0开始，每次+1， 从后往前数，从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
#注意，通过下标索引取数据，一定不要超过范围
#错误示范：printl(my_list[3])

#倒序取出
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

#取出嵌套列表的元素
my_list = [ [ 1, 2, 3], [4, 5, 6]]
print(my_list)


#列表常用操作
mylist = ["zhongnan","hunan","zhongnanlin"]
#1.1 查找某元素在列表的下标索引
index = mylist.index("zhongnan")
print(f"zhongnan在列表的下标索引值为：{index}")
#1.2如果被查找元素不存在会报错
"""
index = mylist.index("nihao")
print(f"nihao在列表的下标索引值为：{index}")
"""

#2.修改特定下标索引的值
mylist[0] = "hunankeji"
print(f"列表被修改元素后，结果是{mylist}")

#3.在指定下标位置插入新元素
mylist.insert(1,"best")
print(f"列表插入元素后，结果是{mylist}")

#4.在列表尾部追加···单个···新元素
mylist.append("hunanzhongyiyao")

print(f"追加了元素后，结果是J{mylist}")

#5.在列表尾部追加···一批···新元素
mylist2 = [1,2,3]
mylist.extend(mylist2) #type:ignore
print(f"追加一个新列表后，结果是:{mylist}")

#6.删除下表索引的元素（两种方式）
mylist = ["nanhua","hunanwenli","zhangshaligong"]
#6.1 方式1：del 列表[下标]
del mylist[2]
print(f"delete后：{mylist}")
#6.2 方式2：列表.pop(下标)
mylist = ["nanhua","hunanwenli","zhangshaligong"]
elment = mylist.pop(2)
print(f"pop delete elment为：{elment}")

#7.删除某个元素在列表中的第一个匹配项
mylist = ["nanhua","hunanwenli","zhangshaligong"]
mylist.remove("hunanwenli")
print(f"remove移除元素后，结果为：{mylist}")

#8.清空列表
mylist.clear()
print(f"clear后的结果是：{mylist}")

#9.统计列表内某元素的数量
mylist = ["zhongnanlin","zhongnanlin","zhangshaligong"]
count = mylist.count("zhongnanlin")
print(f"zhongnanlin数量是：{count}")

#10.统计列表中全部的元素数量
mylist = ["nanhua","hunanwenli","zhangshaligong"]
count1 = len(mylist)
print(f"列表中总元素数量为：{count}个")



#list列表循环
def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量：通过下标索引来控制，默认0
    # 每一次循环将下标苏姚


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """



#列表操作练习
# 1. 定义这个列表，并用变量接收它， 内容是：[21, 25, 21, 23, 22, 20]
mylist = [21, 25, 21, 23, 22, 20]

# 2. 追加一个数字31，到列表的尾部
mylist.append(31)

# 3. 追加一个新列表[29, 33, 30]，到列表的尾部
mylist.extend([29, 33, 30])
# 4. 取出第一个元素（应是：21）
num1 = mylist[0]
print(f"从列表中取出来第一个元素，应该是21，实际上是：{num1}")

# 5. 取出最后一个元素（应是：30）
num2 = mylist[-1]
print(f"从列表中取出来最后一个元素，应该是30，实际上是：{num2}")

# 6. 查找元素31，在列表中的下标位置
index = mylist.index(31)
print(f"元素31在列表的下标位置是：{index}")
print(f"最后列表的内容是：{mylist}")


"""
扩展列表的sort方法
在学习了将函数作为参数传递后，我们可以学习列表的sort方法来对列表进行自定义排序
"""

# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 排序，基于带名函数
# def choose_sort_key(element):
#     return element[1]
#
# my_list.sort(key=choose_sort_key, reverse=True)
# 排序，基于lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)

print(my_list)
