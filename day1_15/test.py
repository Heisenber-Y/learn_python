from sys import float_info
import os
import time
import random
# def fib(b):
#     a,b=0,1
#     for _ in range(b):
#         a,b=b,a+b
#         yield a 


        

def main(code_len):
    # for i in fib(20):
    #     print(i)
        
    # str1="hello,world"
    # print(str1.find("or"))
    # list=[1,2,3,4,5]
    # print(list)
    # list2=['hello']*5
    # print(list2)
    # fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    # fruits += ['pitaya', 'pear', 'mango']
    # for fruit in fruits:
    #     print(fruit.title(),end=" ")
    # print()     
    # for i in fruits[0:4]:
    #     print(i)
    # list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    # list2=sorted(list1)
    # list3=sorted(list1,reverse=True)
    # print(list1)
    # print(list2)
    # print(list3)
    # f=[x for x in range(1,10)]
    # print(f)
    # f = [x+y for x in '1' for y in '1234567']
    # print(f)
    # scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # # print(scores['骆昊'])
    # for i in scores:
    #     print(i,scores[i])

    # content = '北京欢迎你为你开天辟地…………'
    # while True:
    #     os.system('cls')
    #     print(content)
    #     time.sleep(2)
    #     content = content[1:] + content[0]

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos=len(all_chars)-1
    code=''
    for _ in range(code_len):
        index=random.randint(1,last_pos)
        code+=all_chars[index]
    print(code)
        







if __name__ == '__main__':
    main(10)
    