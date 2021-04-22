#字符串和常用数据结构

#
def main():
     str1 = "hello, world!"
     print(len(str1))
#     print(str1.capitalize())
#     print(str1.upper())
#     print(str1.lower())
#     print(str1.find('or'))
#     print(str1.find('shit'))
#     print(str1.index('or'))
#    # print(str1.index('shit'))
#     print(str1.startswith('He'))
#     print(str1.startswith('he'))
#     print(str1.endswith('ld!'))
#     print(str1.center(50,'*'))
#     print(str1.rjust(50,'*'))
#
#     str2='abc123456'
#     print(str2[2])
#     print(str2[2:5])
#     print(str2[2::2])
#     print(str2[::2])
#     print(str2[::-1])
#     print(str2[-3:-1])
#
#     print(str2.isdigit())
#     print(str2.isalpha())
#     print(str2.isalnum())
#
#     str3='  jackfrued@126.com '
#     print(str3)
#     print(str3.strip())
#

if __name__=='__main__':
     main()


#定义列表、使用下标访问列表元素以及添加和删除元素的操作。
# def main():
#     list1=[1,3,5,7,100]
#     print(list1)
#     list2=['hello']*5
#     print(list2)
#     # 计算列表长度(元素个数)
#     print(len(list1))
# # 下标(索引)运算
#     print(list1[0])
#     print(list1[4])
#
#     print(list1[-1])
#     print(list1[-3])
#
#
#     list1[2]=300
#     print(list1)
#
#     # 添加元素
#     list1.append(200)
#     list1.insert(1,400)
#     list1 += [1000,4000]
#     print(list1)
#     list1.remove(1)
#     print(list1)
#     if 1234 in list1:
#         list1.remove(1234)
#     del list1[0]
#     print(list1)
#
#     list1.clear()
#     print(list1)
# if __name__=='__main__':
#     main()

#和字符串一样，列表也可以做切片操作，
# 通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表，代码如下所示。

#下面的代码实现了对列表的排序操作。

# def main():
#     list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
#     list2 = sorted(list1)
#     # sorted函数返回列表排序后的拷贝不会修改传入的列表
#     # 函数的设计就应该像sorted函数一样尽可能不产生副作用
#     list3=sorted(list1,reverse=True)
#     list4=sorted(list1,key=len)
#     print(list1)
#     print(list2)
#     print(list3)
#     print(list4)
#     list1.sort(reverse=True)




#我们还可以使用列表的生成式语法来创建列表，代码如下所示。

#除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，
# 就是通过`yield`关键字将一个普通函数改造成生成器函数。
# 下面的代码演示了如何实现一个生成[斐波拉切数列](https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97)的生成器。所谓斐波拉切数列可以通过下面[递归](https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92)的方法来进行定义：

# def fib(n):
#     a,b=0,1
#     for _ in range(n):
#         a,b=b,a+b
#         yield a
#
# def main():
#     for val in fib(20):
#         print(val)
#
#
# if __name__ == '__main__':
#     main()


#Python 的元组与列表类似，
# 不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。
# 顾名思义，我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据。
# 下面的代码演示了如何定义和使用元组。

# def main():
#     # 定义元组
#     t = ('骆昊', 38, True, '四川成都')
#     print(t)
#     # 获取元组中的元素
#     print(t[0])
#     print(t[1])
#  # 遍历元组中的值
#     for x in t:
#         print(x)
#     # 重新给元组赋值
#     # t[0] = '王大锤'  # TypeError
#     # 变量t重新引用了新的元组原来的元组将被垃圾回收

#   # t[0]='1'
#     t=('1','2','3','4')
#     print(t)
# # 将元组转换成列表
#     person= list(t)
#     print(person)
#     person[1]='99'
#     print(person)
# # 将列表转换成元组
#     fruits=['a','b','c']
#     fruits_tuole=tuple(fruits)
#     print(fruits_tuole)

# if __name__=="__main__":
#     main()



#使用集合

# def main():
#     set1={1,2,3,2}
#     print(set1)
#     print('Length= ',len(set1))
#     set2=set(range(1,10))
#     print(set2)
#     set1.add(4)
#     set2.add(5)
#     print('----')
#     set2.update([11,12])
#     print(set1)
#     print(set2)
#     set2.discard(5)
#     print('----')
#     # remove的元素如果不存在会引发KeyError
#     if 4 in set2:
#         set2.remove(4)
#     print(set2)
#
# #遍历集合容器
#
#     for elem in set((1,2,3,4,3,1)):
#         print(elem**2,end=' ')
#     print()
#
#     #将元祖转换成集合
#
#     set3= set((1,2,3,4,5))
#     print('------')
#     print(set3)
#     # 集合的交集、并集、差集、对称差运算
#     print(set1&set2)
#     print(set1|set2)
#     print(set1-set2)
#     print(set1^set2)
# # 判断子集和超集
#     print(set2<=set1)
#     print(set3<=set1)
#     print(set1>=set3)
#     print(set1>=set2)
#
# if(__name__)=="__main__":
#      main()


#使用字典


# def main():
#     scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
#     #通过键可以获取字典中对应的值
#     print(scores['骆昊'])
#     print(scores['狄仁杰'])

# if __name__=='__main__':
#     main()










