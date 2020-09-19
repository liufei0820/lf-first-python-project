#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-05 17:45
# @Author  : fei.liu

def perb():
    a, b = 0, 1
    while b < 1000:
        print(b, end=", ")
        a, b = b, a + b


if __name__ == '__main__':
    print(perb())

