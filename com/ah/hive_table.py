#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 19:38
# @Author  : fei.liu


from hdfs.client import Client
from pyhive import hive
import pandas as pd


HIVE_HOST = 'ailand-hive'
HIVE_PORT = 10000
HIVE_USER = 'hdfs'

HADOOP_HOST = 'http://namenode.ailand:50070'
HADOOP_USER = 'hdfs'

PYTHON_API_MIDDLE_PATH_BASE_DIR = '/dds/py/tmp-result'

client = Client(HADOOP_HOST, HADOOP_USER)


def read_data(database, table, condition="", limit=""):
    conn = hive.connect(host=HIVE_HOST, port=HIVE_PORT, username=HIVE_USER, database=database)
    cursor = conn.cursor()
    sql_str = 'select * from ' + table
    if condition.strip() != '':
        sql_str = sql_str + ' where ' + condition
    if limit.strip() != '':
        sql_str = sql_str + ' ' + limit

    cursor.execute(sql_str)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    return df


def save_data(database, table, file):
    file_hdfs_path = get_hdfs_path(database=database, file=file)
    file_local_path = get_local_path(file)
    client.upload(file_hdfs_path, file_local_path, overwrite=True)
    save_conn = hive.connect(host=HIVE_HOST, port=HIVE_PORT, username=HIVE_USER, database=database)
    cursor = save_conn.cursor()
    sql_str = 'load data inpath \'' + file_hdfs_path + '\'into table ' + table
    cursor.execute(sql_str)
    result = cursor.fetchall()
    return result


def get_local_path(file):
    return '/opt/workspace/' + file


def get_hdfs_path(database, file):
    return PYTHON_API_MIDDLE_PATH_BASE_DIR + '/' + database + '/' + file


def save_file(data, file):
    data.to_csv(file, index=False, sep=',', header=False)
