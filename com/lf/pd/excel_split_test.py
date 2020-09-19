#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 18:36
# @Author  : fei.liu

import os
import pandas as pd

work_dir = r'/Users/apple/Documents/git-source/python-source/my-python-project/resources'
split_dir = f'{work_dir}/splits'

if not os.path.exists(split_dir):
    os.mkdir(split_dir)

## 将一个文件拆分为多个小文件
df_source = pd.read_excel(f'{work_dir}/crazyant_blog_articles_source.xlsx')

# 总数
total_count = df_source.shape[0]

# 每个人的任务数
user_names = ['xiao_shuai', 'xiao_wang', 'xiao_ming', 'xiao_lei', 'xiao_ho', 'xiao_hong']

print(user_names)

split_size = total_count // len(user_names)

if total_count % len(user_names) != 0:
    split_size += 1

df_subs = []


for idx, user_name in enumerate(user_names):
    # iloc的开始索引
    begin = idx * split_size
    # iloc的结束索引
    end = begin + split_size
    # 实现df安装iloc划分
    df_sub = df_source.iloc[begin:end]
    df_subs.append((idx, user_name, df_sub))

for idx, user_name, df_sub in df_subs:
    file_name = f'{split_dir}/crazyant_blog_articles_{idx}_{user_name}.xlsx'
    df_sub.to_excel(file_name, index=False)

# print(split_size)

# print(df_source.index)
# print(df_source.head())




