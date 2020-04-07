# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/06/03:39
# @Author :Yuye
# @File   :Process_control.py

print("请选择你今天要吃啥")
a = input("只能输入数字：")
flag = int(a)
if flag == 1:
    print("吃奶")
elif flag == 2:
    print("吃饭")
elif flag == 3:
    print("吃大餐")
else:
    print("不吃东西")