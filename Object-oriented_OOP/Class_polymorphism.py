# -*- coding: utf-8 -*-
#@Pjname ;PythonBasicLearning
#@Time   :2020/04/01/16:47
#@Author :Jiuyi
#@File   :Class_polymorphism.py

class Animall(object):
    def kind(self):
        print("kind: Animall")

class Dog(Animall):
    def king(self):
        print("kind: Dog")

class Cat(Animall):
    def kind(self):
        print("kind: Cat")


def show_kind(animal):
    animal.kind()



dog = Dog()
cat = Cat()
show_kind(dog)
show_kind(cat)