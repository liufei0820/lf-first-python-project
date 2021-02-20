#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-21 17:14
# @Author  : fei.liu

f = lambda x: x + x

r = f(2)
print(r)

# map函数
map_demo = map(lambda x: x + x, [1, 2, 3, 4])
print(map_demo)
print(list(map_demo))