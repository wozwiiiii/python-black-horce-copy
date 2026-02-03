#字典的基本语法
#字典的定义
my_dict1 = {"wanglihong":99,"zhoujielun":88,"linjunjie":89}
#定义空子典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1},类型是：{type(my_dict1)}")
print(f"字典1的内容是：{my_dict2},类型是：{type(my_dict2)}")
print(f"字典1的内容是：{my_dict3},类型是：{type(my_dict3)}")


#定义重复Key的字典
my_dict1 = {"wanglihong":99,"wanglihong":78,"linjunjie":98}
print(f"重复key的字典内容是：{my_dict1}")

#从字典中基于key获取value
my_dict1 = {"wanglihong":99,"zhoujielun":88,"linjunjie":89}
score = my_dict1["wanglihong"]
print(f"wanglihong的考试分数为：{score}")
score = my_dict1["zhoujielun"]
print(f"zhoujielun的考试分数是：{score}")


#定义嵌套字典
stu_score_dict = {
    "wanglihong":{
        "chinese":77,
        "math":88,
        "english":99
    }, "zhoujielun":{
        "chinese":88,
        "math":77,
        "english":66
}, "linjunjie":{
    "chinese":88,
    "math":70,
    "english":60
}
}
print(f"学生的成绩为：{stu_score_dict}")


#从嵌套中获取数据
score = stu_score_dict["zhoujielun"]["chinese"]
print(f"周杰轮的语文分数是：{score}")
score = stu_score_dict["linjunjie"]["english"]
print(f"林俊节的英语分数是：{score}")



#字典的常用操作
my_dict = {"zhoujielun":99,"linjunjie":88,"zhangxueyou":87}

#新增元素
my_dict["zhangxinzhe"] = 66
print(f"字典经过新增元素后，结果：{my_dict}")

#更新元素
my_dict["zhoujielun"] = 90
print(f"更新后，结果：{my_dict}")

#删除元素
score = my_dict.pop("zhoujielun")
print(f"字典中移除了一个元素，结果：{my_dict},zhoujielun的考试分数是：{score}")

#清空元素
my_dict.clear()
print(f"字典被清空，内容是：{my_dict}")

#获取全部的key
my_dict = {"zhoujielun":99, "linjunjie":89, "zhangxueyou":88, "wanglihong":90}
keys = my_dict.keys()
print(f"字典中全部的keys是：{keys}")

#遍历字典
#方式1：通过获取到的全部key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

#方式2：直接对字典进行for循环，每次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{my_dict[key]}")

#统计字典内的元素数量，len()函数
num = len(my_dict)
print(f"字典中的元素有：{num}个")




#练习题
"""
简易版年终奖励发放
"""
#使用字典，记录每个人的信息
info_dict = {
    "小明":{
        "部门": "研发部",
        "工作年限":2,
        "总薪资":100000,
        "级别":3
    },
    "小美":{
        "部门": "项目部",
        "工作年限":3,
        "总薪资":190000,
        "级别":4
    },
"小刚":{
        "部门": "人事部",
        "工作年限":5,
        "总薪资":1900000,
        "级别":7
    }
}

for key in info_dict:
    if info_dict[key]["级别"] <=3:
        info_dict[key]["级别"] += 1
        print(f"很抱歉的级别还没有到，所以没有奖励，但是您的级别将会升为{info_dict[key]["级别"]} ，未来将会得到更高的奖励")
    else:
         info_dict[key]["总薪资"] += 10000

print(f"最后薪资为：{info_dict}")   
          


"""
演示字典的课后练习：升职加薪，对所有级别为1级的员工，级别上升1级，薪水增加1000元
"""

# 组织字典记录数据
info_dict = {
    "王力鸿": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰轮": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊节": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学油": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德滑": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

print(f"员工在升值加薪之前的结果：{info_dict}")

# for循环遍历字典
for name in info_dict:
    # if条件判断符合条件员工
    if info_dict[name]["级别"] == 1:
        # 升职加薪操作
        # 获取到员工的信息字典
        employee_info_dict = info_dict[name]
        # 修改员工的信息
        employee_info_dict["级别"] = 2    # 级别+1
        employee_info_dict["工资"] += 1000    # 工资+1000
        # 将员工的信息更新回info_dict
        info_dict[name] = employee_info_dict

# 输出结果
print(f"对员工进行升级加薪后的结果是：{info_dict}")
