#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-19 09:32
# @Author  : fei.liu

import pandas as pd

path = r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/baidu_stocks.xlsx'

df = pd.read_excel(path, index_col='datetime', parse_dates=True)
df.sort_index(inplace=True)


print(df.head())


