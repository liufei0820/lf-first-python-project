#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-21 15:02
# @Author  : fei.liu

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
    print("demo1 函数运行")


# function_demo1()


def args_is_str(function_name):
    def wrapper(a):
        t = type(a)
        if not isinstance(t(), str):
            print("参数错误")
        else:
            function_name(a)

    return wrapper


@args_is_str
def function_demo2(args):
    print(args)


# function_demo2("a")



def max_runtime(timeout):
    def out_wrapper(function_name):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            i = function_name()
            end_time = time.time()
            use_time = end_time - start_time

            if use_time > timeout:
                print("函数运行超时")

            return i
        return wrapper
    return out_wrapper


@max_runtime(timeout=1)
def function_demo3(*args, **kwargs):
    time.sleep(2)
    print("demo3 运行")
    return 1


function_demo3()
















