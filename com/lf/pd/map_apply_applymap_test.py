#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 20:48
# @Author  : fei.liu

import pandas as pd

stocks = pd.read_excel(r"/Users/apple/Documents/git-source/python-source/my-python-project/resources/互联网公司股票.xlsx")

dict_company_names = {'bidu': '百度',
                      'baba': '阿里巴巴',
                      'iq': '爱奇艺',
                      'jd': '京东'}

# stocks['公司中文1'] = stocks['公司'].str.lower().map(dict_company_names)
# stocks['公司中文2'] = stocks['公司'].map(lambda x: dict_company_names[x.lower()])
#
# stocks['公司中文3'] = stocks['公司'].apply(lambda x: dict_company_names[x.lower()])
# print(stocks.head())

## applymap用于DataFrame所有值的转换
sub_df = stocks[['收盘', '开盘', '高', '低', '交易量']]
print(sub_df.applymap(lambda x:int(x)))
# print(sub_df.head())