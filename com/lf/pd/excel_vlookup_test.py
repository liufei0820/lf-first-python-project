#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-17 22:23
# @Author  : fei.liu

'''
背景：
    1、有两个excel，有一个相同的列
    2、按照这个相同的列进行合并成一个大的excel，即lookup功能，要求：
        （1）1只需要第二个excel的少量列，比如40个列里挑选2列
        （2）新增的来自第二个excel的列需要放到第一个excel指定的列后面
    3、将结果输出到一个新的excel
'''

import pandas as pd

df_grade = pd.read_excel(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/学生成绩表.xlsx')

df_sinfo = pd.read_excel(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/学生信息表.xlsx')

df_sinfo = df_sinfo[['学号', '姓名', '性别']]

df_merge = pd.merge(left=df_grade, right=df_sinfo, left_on="学号", right_on="学号")

new_columns = df_merge.columns.to_list()

for name in ["姓名", '性别'][::-1]:
    new_columns.remove(name)
    new_columns.insert(new_columns.index("学号") + 1, name)

df_merge = df_merge.reindex(columns=new_columns)

# print(df_merge.head())

df_merge.to_excel(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/学生信息成绩表.xlsx', index=False)
