#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 20:01
# @Author  : fei.liu

import pandas as pd

stocks = pd.read_excel(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/互联网公司股票.xlsx')

# print(stocks.shape)
# print(stocks.head())
# print(stocks['公司'].unique())

# print(stocks.index)

## series MultiIndex
# ser = stocks.groupby(['公司', '日期'])['收盘'].mean()
# print(ser.index)
# print(ser.unstack())
# print(ser.reset_index())

# print(ser.loc['BIDU'])
# print(ser.loc[('BIDU', '2019-10-02')])
# print(ser.loc[:,'2019-10-02'])

## DataFrame MultiIndex
stocks.set_index(['公司', '日期'], inplace=True)
stocks.sort_index(inplace=True)
# print(stocks)

'''
    重要知识：
    在选择数据时：
        元组(key1, key2)代表刷选多层索引，其中key1是索引第一级，key2是第二级，比如key1=JD，key2=2019-10-02
        列表[key1, key2]代表同一层的多个KEY，其中key1和key2是并列的同级索引，比如key1=JD,key2=BIDU
'''
# print(stocks.loc['BIDU'])
# print(stocks.loc[('BIDU', '2019-10-02')])
# print(stocks.loc[('BIDU', '2019-10-02'), '开盘'])

# slice(None) 代表刷选这一索引的所有内容
# print(stocks.loc[(slice(None), ['2019-10-02', '2019-10-03']), :])
print(stocks.reset_index())