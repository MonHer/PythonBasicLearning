# -*- coding: utf-8 -*-
#@Pjname ;PythonBasicLearning
#@Time   :2020/03/31/23:09
#@Author :Jiuyi
#@File   :make.py

def make (size, *tooings):
    print("make a" + str(size)+"inch pizza")
    for tooing in tooings:
        print(tooing)