"""使用变量保存数据并进行算术运算

Version 1.0
Author yml
"""
a=321
b=123
print(a+b)
print(b-a)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

"""
使用input()函数获取键盘输入
使用int()进行类型转换
用占位符格式化输出的字符串
Version 1.0
Author yml
"""
#
# a=int(input('a= '))
# b=int(input('b= '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %d' % (a, b, a / b))




"""
使用type()检查变量的类型
Version 1.0
Author yml
"""

# a=100
# b=12.345
# c=1+5j
# d='hello world'
# e=True
# f=int(1.2)
# g=str(1)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))


"""使用运算符"""

"""
a=5
b=10
c=3
d=4
e=5
a +=b #15
a -=c #12
a *=e #48
a /=e #12

print("a= ",a)
print("b=",b)

flag1=3>2
flag2=2<1
flag3=flag1 and flag2
flag4=flag1 or flag2
flag5=not flag1

print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)
"""


#华氏温度转摄氏温度3

# f=float(input("请输入华氏温度:"))
# c=(f-32)/1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))


"""输入半径计算圆的周长和面积"""
# import math
# redius=float(input('请输入圆的半径='))
# perimeter=2* math.pi*redius
# area=math.pi*redius*redius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)
# print(math.pi)

"""输入年份判断是不是闰年"""
# year=int(input('请输入年份'))
# is_leap=(year % 4==0 and year % 100 !=0 or year %400 ==0)
# print(is_leap)
