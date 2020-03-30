# -*- coding: utf-8 -*-
#@Pjname ;PythonBasicLearning
#@Time   :2020/03/31/00:12
#@Author :Jiuyi
#@File   :For_loop.py

# for循环语句

for letter in "python hello word" :
    print(letter)

# 编历列表
fruits = ['apples','grape','cherry','peach']

for fruit in fruits :
    print(fruit)
    print(type(fruits))
    print("in for")
print('Done')

# 重复循环一定次数 range() 左闭右开写法

for num in range(0,20):
    print(num)