#定义元组
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是{t1}")
print(f"t2的类型是：{type(t2)},内容是{t2}")
print(f"t3的类型是：{type(t3)},内容是{t3}")

#定义单个元素的元组
t4 = ("hello")
print(f"t4的类型是：{type(t4)},内容是{t4}")

#元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是{t5}")

#下标索引取出内容
num = t5[1][2]
print(f"从中取出来的数据是：{num}")

#元组的操作
#1.index查找方法
t6 = ("中南林", "湖南科技", "农大")
index1 = t6.index("中南林")
print(f"在t6中查找中南林，其下标是：{index1}")

#2.count统计方法
t7 = ("中南林","中南林","湖南科技","长沙理工")
num = t7.count("中南林")
print(f"在t7中，中南林的数量为：{num}")      

#3.len函数统计元组元素数量
t8 = ("xiaoming", "xiaohong", "xiaongang", "xiaomei")
num = len(t8)
print(f"t8中元素数量为：{num}")

"""
4.修改元素内容(不能直接如同列表修改元素一样修改元组里的内容
)
t8[0] = "itcast" 
print(f"t8为：{t8}")
"""


#元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1

for element in t8:
    print(f"元组t8元素有：{element}")


#定义一个元组，其中嵌套了列表，可修改列表中元素
t9 = (1,2,["zhongnanlin" , "changshaligong"])
print(f"t9的内容是：{t9}")

t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是：{t9}")