# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/02/23:46
# @Author :Jiuyi
# @File   :Read_and_write.py

import time

#  打开文件
f1 = open(r'lop.txt')
print(f1)
# 读取文件
lines = f1.readlines()  # 读取所有
print(lines)
# 读取一行
# kinship = f1.readline()
# print(kinship)
# 关闭文件
f1.close()

# # 写文件
lisers = ['abc\n', 'xjhkjdfb\n', "hvjdh\n"]
f2 = open(r'lop.txt', 'w')
f2.write('789654')
print(f2)
f2.close()

# 追加文件

f3 = open(r'lop.txt', 'a')
f3.writelines(lisers)
f3.close()

# 新建文件
l = time.time()
f4 = open("jj.txt", 'x')
f4.writelines(lisers)
f4.close()
