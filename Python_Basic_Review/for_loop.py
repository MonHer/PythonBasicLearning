# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/06/03:46
# @Author :Yuye
# @File   :for_loop.py

from collections import Counter

# 凡是多个的都可以通过循环把每一个取出来，[1,100）,'abcedefg', ["apple", "zip", "banana", "peach"]
for year in range(1, 100):
    print("我活了"+str(year)+"年")

str1 = 'abdkxjsl'
for i in str1:
    print('_'+i, end='')

lists = ["apple", "zip", "banana", "peach"]
for item in lists:
    print("我今天吃了"+item)

# 列表翻转
print("**********")
print(list(reversed(lists)))
print(list(sorted(lists)))

li = [x for x in range(10) if x % 2 == 0]
print(li)


lists2 = lists*2
print(lists2)

# 统计重复的的值的个数
my_couter = Counter(lists2)
print(my_couter.most_common())