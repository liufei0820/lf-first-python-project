#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 10:10
# @Author  : fei.liu

import pandas as pd

df = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/beijing_tianqi_2018.csv')


# print(df['bWendu'].str.isnumeric())

print(df['ymd'].str.replace('-', '').str.slice(0, 6))


def get_nianyueri(x):
    year, month, day = x['ymd'].split('-')
    return f"{year}年{month}月{day}日"

df['中文日期'] = df.apply(get_nianyueri, axis=1)
print(df)