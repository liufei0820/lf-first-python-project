#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 16:21
# @Author  : fei.liu

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                    'D':['D0', 'D1', 'D2', 'D3'],
                    'E':['E0', 'E1', 'E2', 'E3']})

df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'],
                    'B':['B4', 'B5', 'B6', 'B7'],
                    'C':['C4', 'C5', 'C6', 'C7'],
                    'D':['D4', 'D5', 'D6', 'D7'],
                    'F':['F4', 'F5', 'F6', 'F7']})

# print(pd.concat([df1, df2]))
# print(pd.concat([df1, df2], ignore_index=True, join='inner'))

s1 = pd.Series(list(range(4)), name="F")
# print(pd.concat([df1, s1], axis=1))

s2 = df1.apply(lambda x:x['A'] + '_GG', axis=1)
s2.name = 'G'
print(pd.concat([df1, s1, s2], axis=1))

