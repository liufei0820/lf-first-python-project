#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-10 15:23
# @Author  : fei.liu

import pandas as pd

# 读取excel
studf = pd.read_excel(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/student_excel.xlsx', skiprows=2)

# print(studf)

# 检测空值
# print(studf.isnull())

# print(studf['分数'].isnull())

# 刷选没有空分数的所有行
# print(studf.loc[studf['分数'].notnull(), :])

# 删除掉全是空值的列
studf.dropna(axis='columns', how="all", inplace=True)

# 删除全是空值的行
studf.dropna(axis='index', how='all', inplace=True)

# 将分数列为空的值填充为0
# print(studf.fillna({'分数': 0}))
studf.loc[:, '分数'] = studf['分数'].fillna(0)

# 将姓名的缺失值填充
studf.loc[:, '姓名'] = studf['姓名'].fillna(method='ffill')

studf.to_excel(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/student_excel_clean.xlsx', index=False)

# print(studf)

