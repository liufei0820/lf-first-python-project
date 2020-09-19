#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-06 08:23
# @Author  : fei.liu

# n = 100
# count = 0
# sum = 0
# while count <= n:
#     sum += count
#     count += 1
#
# # print(sum)
#
# for a in range(2,2):
#     print(a)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
