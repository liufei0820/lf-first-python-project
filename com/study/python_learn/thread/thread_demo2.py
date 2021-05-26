#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-22 17:11
# @Author  : fei.liu

from threading import Thread

class Hello(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello %s" % self.name)


t = Hello("我是一个线程类")
t.start()
print("我是主线程")