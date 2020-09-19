#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-17 08:56
# @Author  : fei.liu

import pandas as pd

df = pd.DataFrame({'pdate': ['2019-12-01', '2019-12-02', '2019-12-04', '2019-12-05'],
                   'pv': [100, 200, 400, 500],
                   'uv': [10, 20, 40, 50]})

# 解决日期索引缺失，第一种方法：reindex
# df_date = df.set_index('pdate')
#
# df_date = df_date.set_index(pd.to_datetime(df_date.index))
#
# pdates = pd.date_range(start='2019-12-01', end='2019-12-05')
#
# df_new = df_date.reindex(pdates, fill_value=0)
#
# print(df_new.head())

# 解决日期索引缺失，第二种方法：resample
df_new2 = df.set_index(pd.to_datetime(df['pdate'])).drop('pdate', axis=1)

df_new2 = df_new2.resample('D').mean().fillna(0)
print(df_new2)
