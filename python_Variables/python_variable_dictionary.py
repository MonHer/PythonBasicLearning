# -*- coding: utf-8 -*-
#@Pjname ;PythonBasicLearning
#@Time   :2020/03/30/01:00
#@Author :Jiuyi
#@File   :python_variable_dictionary.py

# 创建字典
dict1 = {}
dict2 = {"key1":1,"key2":2,'key3':3}
print(type(dict1))
print(type(dict2))

#往字典里面添加值
dict1["key4"] = 4
dict2["key4"] = 2
print(dict1)

#修改字典
dict2["key4"] = 4
print(dict2)

# 删除字典
del dict1

# 字典内置函数
print(len(dict2))
print(str(dict2))
