# -*- coding: utf-8 -*-
# @Pjname ; PythonBasicLearning
# @Time   : 2020/04/11/09:38
# @Author : Yuye
# @File   : Homework_exam_1.py

# 利⽤pip, 安装第三⽅模块requests, 描述你⽤什么⽅法来确认安装是成功的
"""
1.使用pip list命令查看安装包里面是否有requests
2.在命令行输入python，然后 import requests导入包，按下回车键盘
"""

# 把2.918 转化为整形
Decimal = float(2.918)
Decimal = int(Decimal)
# print(Decimal)

# 把10 进制数 18 转化为2进制数
a = 18
a = bin(a)
# print(a)

# ⽤java 替换字符串：”Python is popular” ⾥⾯的Python，并把java 变换成JAVA
popular_Python = str("Python is popular")
popular_JAVA = popular_Python.replace(popular_Python[0:6], "JAVA".upper())
# print(popular_Python)
# print(popular_JAVA)

# 把列表 [1, 2, 3,4 5,6,7,8]⾥⾯的2, 4, 6,8 打印出来
list_nuber = [1, 2, 3, 4, 5, 6, 7, 8]
for x in list_nuber:
    if x % 2 == 0:
        print(x)

# 创建⼀个字典，字典的key分别是name, sex, province ,
# 修改原始province 的值 为新值”江苏
Personal_information = {"name": 'names', "sex": "sexs", 'province': "provinces"}
for key, value in Personal_information.items():
    if key == "province":
        value = str("江苏")
        print(key, ":", value)
