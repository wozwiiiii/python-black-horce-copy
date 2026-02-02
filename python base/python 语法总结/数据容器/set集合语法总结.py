#集合的定义
my_set = {"中南林业科技", "湖南科技", "中南", "华南"}
my_set_empty = set() #定义空集合
print(f"my_set的内容是{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是{my_set_empty}")



#集合的常用操作
#添加新元素
my_set.add("湘潭")
my_set.add("yongzhou")
print(f"my_set after adding,结果是：{my_set}")
#移除元素
my_set.remove("yongzhou")
print(f"after delte,result is:{my_set}")
#随机取出一个元素
my_set = {"中南林业科技", "湖南科技", "中南", "华南"}
element = my_set.pop()
print(f"被取出元素为：{element},取出元素后：{my_set}")


#清空集合，clear
my_set.clear()
print(f"集合被清空后，结果是：{my_set}")


#取两个集合的差集
set1 = {1,2,3}
set2 = {4,5,6,1}
set3 = set.difference(set2)
print(f"消除差集后，集合1的结果是：{set1}")
print(f"消除差集后，集合2结果为：{set2}")

#两个集合合并为1个
set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1.union(set2)
print(f"2集合合并结果为:{set3}")
print(f"合并后集合1：{set1}")
print(f"合并后集合2：{set2}")


#统计集合元素数量
set1 = {1,2,3,4,5,6,7,8,8,8}
num = len(set1)
print(f"集合内的元素数量有：{num}个")

"""
集合的遍历：集合不支持下标索引，
不能用while循环，可以使用for循环
"""
for element in set1:
    print(f"集合的元素有：{element}")



                                                                               
#课后习题
"""
演示集合的课后练习题
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客',
    'itheima', 'itcast', 'itheima', 'itcast', 'best']
"""
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客',
    'itheima', 'itcast', 'itheima', 'itcast', 'best']

# 定义一个空集合
my_set = set()

# 通过for循环遍历列表
for element in my_list:
    # 在for循环中将列表的元素添加至集合
    my_set.add(element)

# 最终得到元素去重后的集合对象，并打印输出
print(f"列表的内容是：{my_list}")
print(f"通过for循环后，得到的集合对象是：{my_set}")
