#静态雷和方法:
from math import sqrt
class tri(object):
    def __init__(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and b+c>a and a+c>b 

    def pre(self):
        return self._a+self._b+self._c 
        
    def area(self):
        half=self.pre()/2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

def main():
    a,b,c=3,4,5
    if tri.is_valid(a,b,c):
        t=tri(a,b,c)
        print(t.pre())
        print(t.area())    
    else:
        print('狗屁11')       
        
                     
if __name__ == '__main__':
    main()
    







# class Person(object):
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age


#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def age(self):
#         return self._age

#      # 修改器 - setter方法
#     @age.setter
#     def age(self,age):
#         self._age=age
#     def play(self):
#         if self._age<=16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
# def main():
#     person=Person('哈哈哈',12)
#     person.play()
#     person.age=22
#     person.play()
# if __name__ == "__main__":
#     main()                


# class Person(object):
#         # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ('_name', '_age', '_gender')

#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     @property
#     def name(self):
#         return self._name 
#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self,age):
#         self._age=age 

#     def play(self):
#         if self._age< 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
# def main():
#     person=Person('asd',22)    
#     person.play()
#     person._gender='s正在玩飞行棋'  

# if __name__ == '__main__':
#     main()
    
        