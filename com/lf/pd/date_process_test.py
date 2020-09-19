#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-17 08:44
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

df.set_index(pd.to_datetime(df['ymd']), inplace=True)

print(df.loc['2018-03'].head())
