# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/03/31/22:12
# @Author :Yuye
# @File   :Function_learning.py

# 定义函数

'''
1：函数代码块以def关键字开头，后接函数标识名称和括号（）
2：任何传入参数和自变量必须放在圆括号（）中间，圆括号之间可以用于定义参数
3：函数的第一行语句可以选择性的使用文档字符串——用于存放函数说明
4：函数的内容以冒号起始，并且缩进
5：retun[]结束函数，选择性返回一个值给对方
'''


# 基本语句
# def <函数名>(参数列表)：
#      <函数语句>
#       retun<返回值>

def hello():
    print("hello,word")


def sum_func(a, b):
    """
    实现加法
    :param a:第一个数字
    :param b: 第二个数字
    :return: 相加的值
    """
    result = a + b
    return result


# 函数调用《记得使用变量接函数》
hello()
he = sum_func(3, 5)
print("3+5=", he)
