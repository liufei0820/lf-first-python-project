#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-19 14:08
# @Author  : fei.liu

import pandas as pd
import numpy as np
import collections

df = pd.DataFrame(
    np.random.random(size=(100000, 4)),
    columns=list('ABCD')
)

# 1、df.iterrow()
# for idx, row in df.iterrows():
#     print(idx, row)
#     print(idx, row['A'], row['B'], row['C'], row['D'])
#     break

# 2、df.itertuples()
# for row in df.itertuples():
#     print(row)
#     print(row.index, row.A, row.B, row.C, row.D)
#     break

# 3、for + zip
for A, B in zip(df['A'], df['B']):
    print(A, B)
    break

# print(df.head())
#