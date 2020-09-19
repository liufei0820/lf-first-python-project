#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-08 21:23
# @Author  : fei.liu

class people:
    name = ''
    age = 0

    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说： 我 %d 岁。" %(self.name, self.age))


class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说： 我 %d 岁, 我在读 %d 年纪" % (self.name, self.age, self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(speaker, student):
    a = ''
    def __init__(self, n , a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample('tim', 25, 80, 4, 'python')
test.speak()