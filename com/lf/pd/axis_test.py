#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 10:59
# @Author  : fei.liu

'''
    pandas的axis参数怎么理解？
    1、axis=0或者"index"
        如果是单行操作，就指的是某一行
        如果是聚合操作，指的是跨行cross rows
    2、axis=1或者"columns"
        如果是单列操作，就指的是某一列
        如果是聚合操作，指的是跨列corss columns

    总结：按哪个axis，就是这个axis要动起来（类似被for遍历），其他的axis保持不动
'''

import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A', 'B', 'C', 'D']
)

# print(df.drop("A", axis=1))
#
# print(df.drop(1, axis=0))

# print(df.mean(axis=0))

# print(df.mean(axis=1))

print(df)
def get_sum_value(x):
    return x['A'] + x['B'] + x['C'] + x['D']

df['sum_value'] = df.apply(get_sum_value, axis=1)
print(df)
