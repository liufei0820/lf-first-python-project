#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-03 20:02
# @Author  : fei.liu

sites = {'google', 'taobao', 'runoob', 'facebook', 'zhihu', 'baidu'}
print(sites)

# 成员测试
if 'runoob' in sites:
    print("runoob 在集合中")
else:
    print("runoob 不在集合中")

# set可以进行结合运算
a = set('abracadabra')
b = set('alacazam')
print(a)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

