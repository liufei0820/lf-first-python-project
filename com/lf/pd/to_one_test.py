#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-15 09:33
# @Author  : fei.liu

import pandas as pd

ratings = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/ratings.dat',
                      sep='::', engine='python', names='UserID::MovieID::Rating::Timestamp'.split('::'))
# print(ratings.head())

# 实现按照用户ID分组，然后对其中一项归一化
def ratings_norm(df):
    '''
    :param df: 每个用户分组的dataframe
    :return:
    '''
    min_value = df['Rating'].min()
    max_value = df['Rating'].max()
    df['Rating_norm'] = df['Rating'].apply(lambda x: (x - min_value) / (max_value - min_value))
    return df

ratings = ratings.groupby("UserID").apply(ratings_norm)
print(ratings.head(100))

