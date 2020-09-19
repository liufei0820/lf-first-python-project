#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 08:41
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

condition = df['ymd'].str.startswith('2018-03')

df.loc[condition, 'wen_cha'] = df['bWendu'] - df['yWendu']

print(df[condition].head())

