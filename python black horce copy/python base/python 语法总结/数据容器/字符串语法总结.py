#字符串
"""
从数据容器的角度，学习字符串
"""

my_str = "zhongnanlinyekeji and chendengji"
#通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，其对应值是：{value}")

#index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and,其起始下标是：{value}")

#replace方法
new_my_str = my_str.replace("chendengji","teacher")
print(f"将字符串{my_str},进行替换后得到：{new_my_str}")

#split方法
my_str = "hello python my first language"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}用split进行划分后：{my_str_list}")


#strip方法
my_str = "   zhongnanlinyekeji and teacher   "
new_my_str = my_str.strip() #不传入参数，去除首尾空格
print(f"字符串{my_str},strip后变为：{new_my_str}")

my_str = "2025zhongnanlinyekejidaxue and teacher"
new_my_str = my_str.strip("2025")
print(f"字符串{my_str}，strip('2025')后结果是：{new_my_str}")


#统计字符串中某字符串出现次数，count
my_str = "zhongnanlinyekejidaxue"
count = my_str.count("n")
print(f"字符串{my_str}中n出现次数为：{count}")


#统计字符串长度，len()
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")




"""
字符串课后练习演示
"itheima itcast boxuegu"
"""
my_str = "itheima itcast boxuegu"
# 统计字符串内有多少个"it"字符
num = my_str.count("it")
print(f"字符串{my_str}中有{num}个it字符")
# 将字符串内的空格，全部替换为字符："|"
new_my_str = my_str.replace(" ", "|")
print(f"字符串{my_str}被替换空格后，结果是：{new_my_str}")
# 并按照"|"进行字符串分割，得到列表
my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}按照|分割后结果是：{my_str_list}")
