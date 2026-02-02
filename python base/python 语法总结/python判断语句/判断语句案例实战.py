#终极猜数字

#构建随机数字
import random
num = random.randint(1,10)

guess_num = int(input("输入你猜测的数字："))

#判断嵌套
#第一次判断
if guess_num == num:
    print("恭喜你第一次就猜对了")
else:
    if guess_num > num:
       print("很抱歉你猜测的数字大了")
    else:
        print("很抱歉你猜的数字小了")

    guess_num = int(input("请再次输入你猜的数字："))
    
#第二次判断
    if guess_num == num:
      print("恭喜你第二次猜对了")   
    else:
        if guess_num > num:
          print("很抱歉你猜测的数字大了")
        else:
          print("很抱歉你猜的数字小了")

        guess_num = int(input("请再次输入你猜的数字："))   

#第三次判断
        if guess_num == num:
          print("恭喜你第三次猜对了")
        else:
          print("很抱歉，还是猜测错了，你没有机会了")

 
