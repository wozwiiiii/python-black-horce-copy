"""
演示json数据和python字典的相互转化
"""

import json
#准备列表，列表中每一个元素都是字典
data = [{"name":"Tom", "age":28}
        ,{"name":"Mike","age":27}
        ,{"name":"Tommy","age":24}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))       
print(json_str)

#准备字典，将字典转换未json
d = {"name":"zhoujielun","addr":"taibei"}
json_str = json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)

#将json字符串转换为python数据类型[{k: v, k: v},{k: v, k: v}]
s = '[{"name":"zhangdashang","age":11},{"name":"wangdachui","age":13},{"name":"zhaoxiaohu","age":16}]'
l = json.loads(s)
print(type(l))
print(l)

#将json字符串转换为python数据类型{k:v,k:v}
s = '{"name":"周杰伦", "addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)
