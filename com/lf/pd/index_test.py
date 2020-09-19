#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 13:37
# @Author  : fei.liu

import pandas as pd
from sklearn.utils import shuffle

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/ratings.csv')

# print(df.count())

# 使用index查询数据
df.set_index('userId', inplace=True, drop=False)

# print(df.loc[500].head())

# print(df.head())

# 查询速度对比
df_shuffle = shuffle(df)
# print(df_shuffle.head())
# 查看索引是否是递增的
# print(df_shuffle.index.is_monotonic_increasing)
# print(df_shuffle.index.is_unique)
# 计时，查询id==500数据性能
# %timeit df_shuffle.loc[500]

# 排序
df_sorted = df_shuffle.sort_index()
# print(df_sorted.index.is_monotonic_increasing)
# print(df_sorted.index.is_unique)

# index自动对齐
s1 = pd.Series([1, 2, 3], index=list('abc'))
s2 = pd.Series([2, 3, 4], index=list('bcd'))
print(s1 + s2)
