#函数和模块的使用
"""
输入M和N计算C(M,N)
"""

# m=int(input('m=: '))
# n=int(input('n=: '))
#
# fm=1
# for num in range(1,m+1):
#     fm *= num
# fn=1
# for num in range(1,n+1):
#     fm *= num
# fmn=1
# for num in range(1,m-n+1):
#     fmn *= fmn
# print(fm // fn //fmn)


"""
    求阶乘

    :param num: 非负整数
    :return: num的阶乘
"""
# num=int(input("请输入：  "))
# def factorial(num):
#     result=1
#     for n in range(1,num+1):
#         result *=n
#     return  result
#
#
# print(factorial(num))


"""
    摇色子

    :param n: 色子的个数
    :return: n颗色子点数之和
    """

# from random import randint
#
#
# def roll_dice(n=2):
#     total=0
#     for i in range(n):
#         total += randint(1,6)
#     return  total
#
# def add(a=0,b=0,c=0):
#     return a+b+c
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))




# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数

# def add(*args):
#     total=0
#     for var in args:
#         total+=var
#     return total
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 3, 5, 7, 9))


#用模块管理函数


"""对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，
因为我们会遇到命名冲突这种尴尬的情况。最简单的场景就是在同一个.py文件中定义了两个同名函数，
由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的。"""
# def foo():
#     print('hello-world')
# def foo():
#     print('haiyoushui ')
#
# foo()

#
# from model1 import foo
#
# foo()
#
# from model2 import foo
# foo()


# from model1 import foo
# from model2 import foo
# foo()



# print('---'.format(__name__))
# def foo():
#     pass
# def bar():
#     pass
#
# if __name__=="__main__":
#     print('call foo()'.format(__name__))
#     foo()
#     print('call bar()')
#     bar()

#我们来讨论一下Python中有关变量作用域的问题。

# def foo():
#     b='hello'
#     def bar():
#         c=True
#         print(a)
#         print(b)
#         print(c)
#     bar()
#
# if __name__ =='__main__':
#     a=100
#     foo()

#通过函数调用修改全局变量`a`的值，但实际上下面的代码是做不到的

# def foo():
#     a=200
#     print(a)
#
# if __name__=='__main__':
#     a=100
#     foo()
#     print(a)


#全局变量
# def foo():
#     global a
#     a=200
#     print(a)
#
# if __name__=="__main__":
#     a=100
#     foo()
#     print(a)

def main():
    print("--")
if __name__=='__main__':
    main()












