#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-20 15:31
# @Author  : fei.liu

from abc import ABCMeta,abstractmethod

class Person:
    def func1(self):
        pass

    # 变量
    name = "ndsfa"
    age = 10000

    # 类私有变量
    __private_args = "private"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(self.name)
        # print(self.age)

    def get_private_args(self):
        return self.__private_args

    @staticmethod
    def my_static_method():
        print("静态方法")


p = Person("lf", 100)
print(p.name)
print(p.age)
print(p.get_private_args())
Person.my_static_method()
p.my_static_method()