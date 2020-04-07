# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/06/04:06
# @Author :Yuye
# @File   :While_loop.py

def while_demo():
    numbers = [10, 11, 12, 13, 14, 15]
    even = []
    odd = []
    while len(numbers):
        number = numbers.pop()
        if (number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)
    return even, odd


print(while_demo())
