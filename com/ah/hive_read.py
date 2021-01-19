#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-12-23 09:56
# @Author  : fei.liu


import numpy as np # 快速操作结构数组的工具
import matplotlib.pyplot as plt  # 可视化绘制
from sklearn.linear_model import LinearRegression  # 线性回归
from pyhive import hive
import pandas as pd


host = '172.18.0.6'
port = 10000
username = 'hive'
def load_hive_df(database, table, count = 0):
    conn = hive.connect(host=host, port=port, username=username, database=database)
    cursor = conn.cursor()
    sql_str = 'select * from ' + table
    if count > 0:
        sql_str = sql_str + 'limit ' + count

    cursor.execute(sql_str)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    return df

def load_hive_np(database, table, count = 0):
    conn = hive.connect(host=host, port=port, username=username, database=database)
    cursor = conn.cursor()
    sql_str = 'select * from ' + table
    if count > 0:
        sql_str = sql_str + 'limit ' + count

    cursor.execute(sql_str)
    result = cursor.fetchall()
    arr = np.array(result)
    return arr
