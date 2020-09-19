#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-05 11:04
# @Author  : fei.liu

str = 'runoob\t12345\tabc'
print("原始字符串：", str)

print("替换\\t符号：", str.expandtabs())

print("使用2个空格替换\\t符号：", str.expandtabs(2))

print("使用3个空格替换\\t符号：", str.expandtabs(3))

print("使用4个空格替换\\t符号：", str.expandtabs(4))

