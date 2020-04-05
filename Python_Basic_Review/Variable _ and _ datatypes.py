# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/06/02:38
# @Author :Jiuyi
# @File   :Variable _ and _ datatypes.py

""" 定义变量 """

# 定义一个 整型(int)
my_int = 10

# 定义一个字符串(str)
""" str，单引号，双引号，三引号都可以，三引号不赋值，算是注释 """
my_str = "I'm love python"

# 定义一个元组(tuple)
""" tuple，固定长度不能变 """
my_tuple = ("python", 17, 8.5, 8.88)

# 定义一个列表(list)
""" list 可变化长度，有序 """
my_list = ["python", 12, 13, 13.14, 520]

# 定义一个字典
""" dict 没有顺序，按照key和value的方式储存 """
my_dict = {"name": "jiuyi", "age": 24, "Hobby": "泡妞"}

""" 一行可以写多个语句，使用分号(;)隔开 """
# 定义一个集合（set）
""" set 元素不能出现重复 """
my_set = {1, 2, 3}; print(dir(my_set))

# 定义一个布尔类型
my_bool = True

"""变量进阶学习"""
# 1：一个值多个变量赋值
a = b = c = 1

# 同时多个值赋值给多个变量
a, b, c = 1, 2, "Yuye"


