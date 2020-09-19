#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-09 18:18
# @Author  : fei.liu

import numpy as np

# s = b'hello world'
# a = np.frombuffer(s, dtype = 'S1')
# print(a)

# x = np.eye(16)
# print(x)
#
# x = np.arange(5, dtype=float)
# # print(x)
#
# a = np.linspace(1, 19, 10)
# b = a.reshape([10, 1])
# print(a.reshape([10, 1]))

# x = np.array([[1,2], [3,4], [5,6]])
# y = x[[0, 1, 2], [0 ,1, 0]]
# print(y)

# x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# print(x)
# print('\n')
# rows = np.array([[0,0],[3,3]])
# print(rows)
# print('\n')
# cols = np.array([[0,2],[0,2]])
# print(cols)
# print('\n')
# y = x[rows, cols]
# print(y)

# x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# print('\n')
# print('大于 5 的元素时： ')
# print(x[x > 5])

# a = np.arange(6).reshape(2,3)
# for x in np.nditer(a.T.copy(order='C')):
#     print (x, end=", " )
# print ('\n')

# a = np.arange(0, 60, 5)
# print(a)

import numpy as np

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [2, 2], [3, 3]])
cols = np.array([[0, 2], [0, 2], [0, 1]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)