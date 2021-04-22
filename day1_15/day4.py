#循环结构


#for-in 循环
"""
用for循环实现1~100求和

Version: 0.1
Author: yml
"""
# sum=0
# for x in range(1,101):
#     sum+=x
#     print(sum)

#- `range(101)`可以产生一个0到100的整数序列。
#- `range(1, 100)`可以产生一个1到99的整数序列。
#- `range(1, 100, 2)`可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。


"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: yml
"""

# sum = 0
# for x in range(2, 101, 2):
#     sum += x
#     print(sum)

#通过循环中使用分支计算相同的功能

# sum=0
# for x in range(1,101):
#     if x%2==0:
#         sum+=x
#     print(sum)


"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
"""

# import  random
# answer = random.randint(1,100)
# counter = 0
# while True :
#     counter +=1
#     number=int(input('请输入 '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('猜对了')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 10:
#     print('你的智商余额明显不足')


"""
输出乘法口诀表(九九表)

Version: 0.1
Author: yml
"""

# for i in range(1,10):
#     for j in range(1,i+1):
#         #print('%d*%d=%d' % (i, j, i * j)
#             print('%d*%d=%d' %(i,j,i*j), end='\t')
#     print('---')


#输入一个数判断是不是素数。

"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: yml
Date: 2018-03-01
"""

# from math import sqrt
# num = int(input("请输入一个数字: "))
# end = int(sqrt(num))
# is_prime = True
#
# for x in  range(2,end + 1):
#     if num % 2==0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)


"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: yml
Date: 2018-03-01
"""

# x=int(input("x= "))
# y=int(input("y= "))
# if x > y :
#     x,y=y,x
# for factor in range(x,0,-1):
#     if x %factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break


"""打印三角形"""


# row = int(input("请输入行数: "))
# for i in range(row):
#     for _ in range(i+1):
#         print('*',end='')
#     print()

row = int(input("请输入行数: "))

# for i in range(row):
#     for j in range(row):
#         if j<row - i -1 :
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()



for i in range(row):
    for _ in range(row -i -1 ):
        print(' ',end='')
    for _ in range(2*i+1):
        print('*',end='')
    print()










