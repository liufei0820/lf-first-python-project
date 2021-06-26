#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 10:53
# @Author  : fei.liu

"""
闭包：简单来说，就是一个外部函数的返回值是内部函数的引用
"""


def outer(a):
    b = 10

    def inner():
        print(a + b)

    # 外部函数的返回值是内部函数的引用
    return inner


inner_func = outer(5)
inner_func()

