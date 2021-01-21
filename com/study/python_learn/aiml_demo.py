#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-20 10:45
# @Author  : fei.liu

import aiml

k = aiml.Kernel()
k.learn("/Users/apple/Documents/git-source/python-source/my-python-project/resources/python_study/std-startup.xml")
k.respond("load aim b")

while True:
    print(k.respond(input("input >> ")))