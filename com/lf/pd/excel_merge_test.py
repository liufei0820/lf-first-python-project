#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 18:59
# @Author  : fei.liu


## 合并多个小excel为一个大excel

import os
import pandas as pd

work_dir = r'/Users/apple/Documents/git-source/python-source/my-python-project/resources'
split_dir = f'{work_dir}/splits'

excel_names = []
for excel_name in os.listdir(split_dir):
    excel_names.append(excel_name)

df_list = []
for excel_name in excel_names:
    excel_path = f"{split_dir}/{excel_name}"
    df_split = pd.read_excel(excel_path)

    # 得到username
    username = excel_name.replace("crazyant_blog_articles_", '').replace('.xlsx', '')[2:]
    print(excel_name, username)
    df_split['username'] = username

    df_list.append(df_split)

df_merged = pd.concat(df_list)

# print(df_merged.shape)
# print(df_merged.head())
# print(df_merged['username'].value_counts())

df_merged.to_excel(f"{work_dir}/crazyant_blog_articles_merged.xlsx", index=False)

