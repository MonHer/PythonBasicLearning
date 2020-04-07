# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/06/04:03
# @Author :Yuye
# @File   :Break_Continue.py

"""
break语句⽤来终⽌循环语句;
continue 语句跳出本次循环，⽽break跳出整个循环
"""

# 跳过某个字母不输出(过滤)  在序列中筛选一下不要的
for letter in 'Python':
    if letter == 'h':
        continue
    print('当前字母 :', letter)


# 在序列中找到自己想要的，一旦找到就不找了
a = 'f'
b = ['a', 'b', 'c', 'd']
for my in b:
    if a == my:
        print("找到！")
        break
else:
    print("没找到！")