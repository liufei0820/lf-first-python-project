#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 11:02
# @Author  : fei.liu

"""
装饰器： （语法糖、注解）
"""

import time


def runtime_noargs(function_name):

    def wrapper():
        start_time = time.time()
        function_name()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


@runtime_noargs
def function_demo1():
    print("demo1函数运行")


# function_demo1()


def args_is_str(function_name):
    def wrapper(a):
        t = type(a)
        if not isinstance(t(), str):
            print("args error")
        else:
            function_name(a)
    return wrapper


@args_is_str
def function_demo2(args):
    print(args)


# function_demo2('aaa')


def many_args(function_name):
    def a(*args):
        print(*args)
        function_name(*args)
    return a


@many_args
def function_demo3(*args):
    print(*args)


# function_demo3(1, 2, 3, 4)


def function_demo4(**kwargs):
    print(kwargs)


function_demo4(name="zhangsan", age=10)
