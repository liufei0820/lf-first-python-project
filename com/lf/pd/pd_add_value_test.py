#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-10 13:38
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

# print(df.head())

# 修改 bWendu、yWendu的值
df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

# 新增列
df.loc[:, 'wencha'] = df['bWendu'] - df['yWendu']

# 新增温度类型列
def get_wendu_type(x):
    if x['bWendu'] > 33:
        return '高温'
    if x['yWendu'] < -10:
        return '低温'
    return '常温'

df.loc[:, 'wendu_type'] = df.apply(get_wendu_type, 1)


# df.assign方法：将温度从摄氏度变成华氏度
new_df = df.assign(
    yWendu_huashi = lambda x : x['yWendu'] * 9 / 5 + 32,
    bWendu_huashi = lambda x : x['bWendu'] * 9 / 5 + 32
)

# 按调节选择分组分别赋值
df['wencha_type'] = ''
df.loc[df['bWendu'] - df['yWendu'] > 10, 'wencha_type'] = '温差大'
df.loc[df['bWendu'] - df['yWendu'] <= 10, 'wencha_type'] = '温差正常'

print(df['wencha_type'].value_counts())
