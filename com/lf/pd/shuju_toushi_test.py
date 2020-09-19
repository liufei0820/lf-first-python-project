#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-16 21:59
# @Author  : fei.liu

import pandas as pd
import numpy as np

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/ratings.dat',
                      sep='::', engine='python', names='UserID::MovieID::Rating::Timestamp'.split('::'))

df['pdate'] = pd.to_datetime(df['Timestamp'], unit='s')

df_group = df.groupby([df['pdate'].dt.month, 'Rating'])['UserID'].agg(pv=np.sum)

# df_stack = df_group.unstack()
#
# print(df_stack.plot())

df_reset = df_group.reset_index()

df_povit = df_reset.pivot('pdate', 'Rating', 'pv')
print(df_povit)
