# -*- coding: utf-8 -*-
# @Pjname ;PythonBasicLearning
# @Time   :2020/04/01/09:55
# @Author :Yuye
# @File   :Class_characteristics.py

# 类的三大特性学习

# 封装
class Animal(object):
    eyes = int(2)

    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def run(self):
        print(self.name + '说：'"星空不问赶路人,时光不负有心人")


# 继承和修改类
class Cat(Animal):
    def eat(self):
        print("我的小鱼你醒了")

    def run(self):
        print(self.name + '说：'"将来的你一定会感谢你今天的努力的")


class Dog(Animal):
    def run(self):
        print(self.name + '说：'"明天不上班")


# cat = Cat("cat", "nibaba")
# cat.run()
# cat.eat()
# 多态

class CatDog(Dog, Cat):
    def run(self):
        Animal.run(self)


cp = CatDog('cat', '倪霸霸')
cp.eat()
cp.run()
