# -*- coding: utf-8 -*-
#@Pjname ;PythonBasicLearning
#@Time   :2020/03/30/22:40
#@Author :Jiuyi
#@File   :Input_and_output.py

# 输入函数input()

age = input("请输入你的年龄:")
print(age)
print(type(age))

age = int(input("请输入你的年龄:"))
print(age)
print(type(age))


#输出函数 print()

print('a','b','c')
print('a','b','c',sep=',')
print('a','b','c',end=';')
