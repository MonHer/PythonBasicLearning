# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/11/14:19
# @Author : Yuye
# @File   : Homework_exam_2.py

# 1. Test_str=“Python was created in 1989, Python is using in AI, big
"""
data, IOT.” 按下列要求对上⾯⽂字做出处理。
1• 把上⾯⽂字中的所有⼤写转化为⼩写
2• 把这段话每个单词放到列表⾥⾯，不能包含空格。
3• 把列表最中间的⼀个单词打印出来。
"""

Test_str = "Python was created in 1989, Python is using in AI, big"
print(Test_str.lower())
TT = Test_str.split()
TT = list(TT)
print(TT)
TT_len = len(TT)
print(TT[5])

# List1=[“python”, 5,6, 8], list2=[“python”,”5”, 6, 8,10],
# 对list1和list2做出如下处理：
'''
1.把上⾯2个list的内容合并成⼀个
2.利⽤set⾥⾯的⽅法，对合并后的list， 去除重复元素。最 后输出是还
是list =[“python”, 5,6, 8,”5”,10] (顺序可以不⼀ 样)
'''
List1 = ["python", 5, 6, 8]
# print(type(List1))
list2 = ["python", "5", 6, 8, 10]
# print(type(list2))
list3 = list2 + List1
print(set(list3))



