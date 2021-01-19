#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-14 15:51
# @Author  : fei.liu

# list
list1 = [1, 2, 3, 4]
# print(list1)
# 访问
print(list1[0])

# 冒泡排序
a = [13, 23, 454, 5, 43, 7567]

for i in range(len(a) - 1):
    for j in range(len(a) - 1 -i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
