#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-08 18:18
# @Author  : fei.liu
import os

ret = os.access("/Users/apple/Documents/git-source/python-source/my-python-project/resources/foo.txt", os.F_OK)
print(ret)

