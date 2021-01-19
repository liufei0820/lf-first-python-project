#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-23 13:25
# @Author  : fei.liu

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A', 'B', 'C', 'D']
)

print(df.dtypes)
