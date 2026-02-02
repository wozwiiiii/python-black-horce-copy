#练习题1：while求1-100的和
sum = 0
i = 1
while i <= 100:
    sum += i
    i +=1
print(f"1-100累计的和为{sum}")

#练习题2：while循环基础案例-猜数字
import random
num = random.randint(1,100)
count = 0
while count <= 100:
    count += 1
    guess_num = int(input("请输入您猜测的数字："))
    if guess_num == num:
        print("恭喜您答对了")
        break
    else:
        if guess_num > num:
            print("您猜测的数字大了")
        else:
            print("您猜测的数字小了")

    #这一步可删        
    print(f"您已经猜测了{count}次")

print(f"恭喜您在猜测了{count}次后找到了正确答案")   


#练习题3：for循环基础案例-数一数有几个a
name = "zhongnanlinyekejidaxue zhong you duoshao dianzixinxiyuwulixueyuan deren"

count = 0

for j in name:
    if j == "i":
        count += 1

print(f"被统计的字符串中一共含有{count}个i")


#练习题4：for及while循环打印九九乘法表
#for循环
#外层循环控制行数
for i in range(1,10):
    #内层循环控制每一行内容
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')

    #外层循环通过print()输出一个回车符    
    print()        


#while循环
#定义外侧循环控制量
i = 1

while i <= 9:

    #定义内层循环控制量
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')  
        j += 1
    i += 1
    print()    #输出空内容，就是输出一个换行