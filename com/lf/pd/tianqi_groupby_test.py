#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 19:42
# @Author  : fei.liu

import pandas as pd
import numpy as np

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

df['month'] = df['ymd'].str[:7]

data = df.groupby('month')['bWendu'].max()

print(df.groupby('month').agg({'bWendu':np.max, 'yWendu':np.min, 'aqi':np.mean}))
# print(data.plot())


