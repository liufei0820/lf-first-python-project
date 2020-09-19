#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-09 20:30
# @Author  : fei.liu


import pandas as pd

filename = r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/pd.csv'

# 设置列索引
# data = pd.read_csv(filename, header=None, names=('a', 'b', 'c', 'd', 'e', 'f', 'g'))

# 设置行索引
# data = pd.read_csv(filename, index_col=None, header=None)

# 设置读取某一列
# data = pd.read_csv(filename, index_col=None, header=None, usecols=[1, 2])

# 设置读取前几行数据
# data = pd.read_csv(filename, index_col=None, header=None).head(5)

# 设置返回第几行第几列的数据
# data = pd.read_csv(filename, index_col=None, header=None).loc[[1,3,5],[2,4]]

# 统计信息
data = pd.read_csv(filename, index_col=None, header=None).describe()

print(data)