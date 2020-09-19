#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 08:56
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

print(df.head())

print(df.loc[271])

print(df['aqi'].sort_values())