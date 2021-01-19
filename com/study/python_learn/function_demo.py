#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-18 15:16
# @Author  : fei.liu

# 自定义函数
def func():
    print("name")
    print(__name__)

# 函数参数
def my_func_1(p1, p2):
    print(p1)
    print(p2)


# 递归：自己调用自己（在函数内部进行调用）
def my_func_2(x):
    # 明确递归结束条件
    if x == 1:
        return 1
    print("计算" + str(x) + "+" + str(x-1))
    return x + my_func_2(x-1)


# 函数的返回值是一个函数
def my_func_3(x):
    if x == 2:
        def inner_func(y):
            print("inner 1 被调用")
            return y * y
    if x == 3:
        def inner_func(y):
            print("inner 2 被调用")
            return y * y * y
    return inner_func


if __name__ == "__main__":
    # func()
    # my_func_1(1, 2)
    # print(my_func_2(5))
    calc = my_func_3(3)
    z = calc(4)
    print(z)
