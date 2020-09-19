#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-09 21:15
# @Author  : fei.liu

import pandas as pd
import numpy as np

filename = r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/pd_row.csv'


data = pd.read_csv(filename, index_col=0, header=0)

column_header = list(data.columns.values)
print(column_header)

# print(data.info)