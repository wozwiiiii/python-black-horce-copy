#演示文件的写入

import time

"""基础语法：
#打开一份文件
f = open("D:/test.txt","w",encoding="UTF-8")

#write 写入
f.write("hello world") #内容写入到内存中

#flush刷新
f.flush()   #将内存中积攒的内容，写入到硬盘文件中

#close关闭
f.close()   #close方法内置了flush功能
"""

#打开一个存在的文件
f = open("D:/test.txt","w",encoding="UTF-8")
#write写入，flush刷新
f.write("chendengji")
#close关闭
f.close()

#演示文件的追加写入
"""基础语法：
# 打开文件，不存在的文件
f = open("D:/test.txt", "a", encoding="UTF-8")
#write写入
f.write("黑马程序员")
#flush刷新
f.flush()
# close关闭
f.close()
"""
# 打开一个存在的文件
f = open("D:/test.txt", "a", encoding="UTF-8")
# write写入、flush刷新
f.write("\nzhongnanlinyekejidaxue")
# close关闭
f.close()