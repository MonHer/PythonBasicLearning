# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/02/10:58
# @Author :Jiuyi
# @File   :Exception_handling.py


# 异常处理
# 捕获单个异常
try:
    filel = open(r'D:\seleniumWebTest\testsuites\test01.py')
    print('filel is open')
except IOError as result:
    print(result)

# 捕获所有异常

try:
    filel = open(r'D:\seleniumWebTest\testsuites\test01.py')
    print('filel is open')
except Exception as result:
    print(result)
else:
    print("no Exception")
finally:
    filel.close()