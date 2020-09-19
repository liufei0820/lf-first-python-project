#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-16 21:09
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')

df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

df['month'] = df['ymd'].str[:7]

def getWenduTopN(df, topn):
    '''
    这个的df，是每个月分组group的df
    :param df:
    :param topn:
    :return:
    '''
    return df.sort_values(by='bWendu')[['ymd', 'bWendu']][-topn:]

print(df.groupby('month').apply(getWenduTopN, topn = 1))

