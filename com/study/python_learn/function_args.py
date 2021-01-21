#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-21 16:45
# @Author  : fei.liu

'''
函数的参数：
-- 必须参数、默认参数、组合参数
-- 函数作为参数
-- 对象作为参数
-- **kwargs 叫做关键字参数
-- *args    可变参数
'''

def funciton(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))


# funciton(1, 2, 3, 4, 5, name=1, age=12)


def function2(a, b, c):
    print(a)
    print(b)
    print(c)


kw = {"a":1, "b":2, "c":3}
# function2(*kw)
function2(**kw)









