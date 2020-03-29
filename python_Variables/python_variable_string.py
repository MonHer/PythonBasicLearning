# -*- coding: utf-8 -*-
#@Pjname ;PythonBasicLearning
#@Time   :2020/03/30/00:14
#@Author :Jiuyi
#@File   :python_variable_string.py

#字符串
str1 = 'abc'
print(str1)

str2  = "abc"
print(str2)

#单引号和双引号的区别
# str3 = 'a'bc' 报错示范
str3 = "a'bc"
print(str3)

str4 = """
我的小鱼你醒了
还认识早晨吗？
昨夜你曾经说，
愿夜幕永不开启。
你的香腮边轻轻滑落的，
是你的泪，还是我的泪？
初吻吻别的那个季节，
不是已经哭过了吗？
我的指尖还记忆着，
你慌乱的心跳。
温柔的体香里，
那一缕长发飘飘。
"""
print(str4)

#字符串索引
#正向
print(str4[0])
print(str4[3])
#反向
print(str4[-0])
print(str4[-3])

#切片
print(str4[0:4])
print(str4[3:15])

#更改字符串
#将字符串强制转为列表
list1 = list(str4)
list1[0] = "硪"
print(list1)
str4 = ''.join(list1)
print(str4)



