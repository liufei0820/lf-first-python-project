#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 19:19
# @Author  : fei.liu


import numpy as np
import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print(df)

# 分组使用聚合函数做数据统计
# 1.1 单个列groupby，查询所有数据列的统计
# print(df.groupby('A').sum())
# print(df.groupby(['A', 'B'], as_index=False).mean())
# print(df.groupby('A').agg([np.sum, np.mean, np.std]))
# print(df.groupby('A')['C'].agg([np.sum, np.mean, np.std]))
# print(df.groupby('A').agg([np.sum, np.mean, np.std])['C'])
print(df.groupby('A').agg({'C':np.sum, 'D':np.mean}))


