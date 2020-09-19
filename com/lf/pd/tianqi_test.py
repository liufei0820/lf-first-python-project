#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-10 10:44
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

# print(df.head())

df.set_index('ymd', inplace=True)

df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

# print(df.dtypes)

# print(df.loc['2018-01-03', 'bWendu'])
#
# print(df.loc['2018-01-03', ['bWendu', 'yWendu']])

# print(df.loc[['2018-01-03', '2018-01-05', '2018-01-09'], ['bWendu', 'yWendu']])
# print(df.loc['2018-01-03':'2018-0130', ['bWendu', 'yWendu']])

# 心中完美天气
# print(df.loc[(df['bWendu'] <= 30) & (df['yWendu'] >= 15) & (df['tianqi'] == '晴') & (df['aqiLevel'] == 1),:])

# lambda 方式
#print(df.loc[lambda df:(df['bWendu'] <= 30) & (df["yWendu"] >= 15), :])

# 自定义函数
def query_my_data(df):
    return df.index.str.startswith('2018-09') & df['aqiLevel'] == 1

print(df.loc[query_my_data,:])
