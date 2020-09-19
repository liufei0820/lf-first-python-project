#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-19 10:56
# @Author  : fei.liu

import pandas as pd
import os

file_dir = r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/blog_access_log'

file_list = []

for file in os.listdir(file_dir):
    file_list.append(pd.read_csv(f'{file_dir}/{file}', sep=" ", header=None, error_bad_lines=False))

df = pd.concat(file_list)

df = df[[0, 3, 6, 9]].copy()

df.columns = ['ip', 'stime', 'status', 'client']

df['is_spided'] = df['client'].str.lower().str.contains('spider')

df_spider = df['is_spided'].value_counts()

df_status = df.groupby('status').size()

print(df_status)

