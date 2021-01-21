#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-21 13:40
# @Author  : fei.liu

'''
多态
多态指的是一类食物有多种形态

多态性
'''

class Animal:
    def run(self):
        raise AttributeError("子类必须实现这个方法")

class Person(Animal):
    def run(self):
        print("人 跑")


person = Person()
person.run()

