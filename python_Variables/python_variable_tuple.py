# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/03/30/00:46
# @Author :Yuye
# @File   :python_variable_tuple.py

# 创建元组
tu1 = ("a", "b")
tu2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tu3 = (1, "a")
tu4 = ()
tu5 = (9)  # 错误写法
print(type(tu5))
tu6 = (9,)

# 访问使用切片

# 内置操作元组
print(len(tu2))  # 个数
print(max(tu2))
print(min(tu2))

# 删除元组
del tu5
print(tu5)
