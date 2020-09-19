#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-08 18:46
# @Author  : fei.liu

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is ', result)
    finally:
        print('executing finally clause')

# divide(2, 1)
#
# divide(2, 0)

divide("2", "1")