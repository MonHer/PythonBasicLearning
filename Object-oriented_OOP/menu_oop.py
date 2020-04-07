# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/03/31/23:50
# @Author :Yuye
# @File   :menu_oop.py

# 定义一个类
class Menu(object):
    Aioli = '蒜泥白菜'
    Pickled_Konjac_Tofu = '酸菜魔芋豆腐'

    def __init__(self, ty, yt):  # 构造函数
        self.ty = ty
        self.yt = yt

    def eat(self):  # 定义方法
        print("123456"+self.ty, self.yt)



# 调用类
I_want_to_eat = Menu("HJDHF", "FDJIH")
I_want_to_eat2 = Menu("KK", "FDSB")
print(I_want_to_eat.Aioli)
print(I_want_to_eat.Pickled_Konjac_Tofu)
I_want_to_eat.eat()
I_want_to_eat2.eat()
