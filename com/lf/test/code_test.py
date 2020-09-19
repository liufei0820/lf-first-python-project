#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-05 11:00
# @Author  : fei.liu

str = '你好'
str_utf8 = str.encode('UTF-8')
str_gbk = str.encode('GBK')

print(str)
print('UTF-8 编码：', str_utf8)
print('GBK 编码：', str_gbk)

print('UTF-8 解码：', str_utf8.decode('UTF-8', 'strict'))
print('GBK 编码：', str_gbk.decode('GBK', 'strict'))
