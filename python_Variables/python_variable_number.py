# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/03/30/00:12
# @Author :Yuye
# @File   :python_variable_number.py

# 数字number
# int
num1 = 2
num2 = 0b101
num8 = 0o24
num16 = 0x3F

# float
float_num1 = 2.345
print(float_num1)
float_num2 = 1.23e9
print(float_num2)

# bool
b_var = True
print(b_var)
b_var1 = False
print(b_var1)
# 注意python中的大小写敏感


# complex
c_num = complex(3, 4)
print(c_num)

# 查看数据类型
# type()


# 运算符
a = 5
b = 2

# 算术运算符
print(a + b)
print(a * b)
print(a ** b)
print(a / b)
print(a // b)  # 取整
print(a % b)  # 取余

# 比较运算符
print(a > b)
print(a <= b)

# 逻辑运算符
print((a > b) and (a < b))
print((a > b) or (a < b))

# 变量命名规则
# 1.变量名通常由字母,数字,下划线组成;
# 2.数字不能作为变量名开头;
# 3.不能以python中的关键字命名;
# 4.变量名要有意义;
# 5.不要用汉字和拼音去命名;
# 6.变量名要区分大小写;
# 7.推荐使用驼峰型(GuessAge或guessAge)和下划线(guess_age)来命名;
# 8.常量通常使用大写来定义.
