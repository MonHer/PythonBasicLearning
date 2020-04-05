# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/06/03:11
# @Author :Jiuyi
# @File   :Data_and_conversion.py

my_str = "I love Python"
my_list = ["python", "java", "lanuage", "age"]
my_list2 = [24, 12, 2.3, 9.7]
my_tuple = ("python", 33, "java", 8.8)
my_dict = {"name": "Jiuyi", "age": 88}
my_list1 = ['a', 'a', 1, 1, 2, 3]
my_set = {1, 2, 3}

a = 10
print(type(a))

""" 数据转换练习 """
# 将int强制转化为str
a1 = str(a)
print(type(a1))

# 将str强制转换为int
print(type(int(a1)))

# list与tuple相互转换
print(tuple(my_list))
print(list(my_tuple))

# list 转成set变量不重复的
print(set(my_list1))

# 字典类型转成set只有key值
print(set(my_dict))

# 字典转成列表，key,value可以单转
print(list(my_dict.values()))

print(list(my_dict))
my_tuple1 = ("one", 1), ('two', 2), ("three", 3)
my_list1_tuple = [('one', 1), ('two', 2), ('three', 3)]
print(my_tuple1)
print(type(my_list1_tuple))
print(dict(my_list1_tuple))

# 将对象x 转成字符串
b = {"name": "jiuyi", "age": 18}
str_b = repr(b)
print(str_b[0:3])

# 用来计算在字符串中的有效Python表达式,并返回一个对象
a = "[1, 2, 3]"
list_a = eval(a)
print(type(list_a))
print(list_a[0])
