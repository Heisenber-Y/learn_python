class  Student(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def study(self,course_name):
#          print('%s正在学习%s.' % (self.name, course_name))
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看岛国爱情大电影.' % self.name)
# def main():
#     stu1=Student('骆昊', 38)
#     stu1.study("Python程序设计")
#     stu1.watch_movie()
#     stu2=Student('aa',14)
#     stu2.study("阿松大")
#     stu2.watch_movie()  
#222
    def __init__(self,foo) -> None:
       self.__foo=foo

    def __bar(self):
        print(self.__foo)
        print('_bar')   
def main():
        test=Student('hello')
        test.__foo()
if __name__ == '__main__':
        main()
                         