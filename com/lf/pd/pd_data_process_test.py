#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-10 14:18
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

# 1、汇总统计
# 1.1 describe
# print(df.describe())

# 1.2 平均值
# print(df['bWendu'].mean())

# 1.3 最大值
# print(df['bWendu'].max())

# 1.4 最小值
# print(df['bWendu'].min())


# 2、唯一去重和按值计数
# 2.1 唯一去重性
# print(df['fengxiang'].unique())

# 2.2 按值统计
# print(df['fengxiang'].value_counts())

# 2.3 协方差和相关系数
print(df.cov())
print(df.corr())
