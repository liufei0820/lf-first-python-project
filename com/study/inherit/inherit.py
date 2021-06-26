#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-24 10:46
# @Author  : fei.liu


class Father:
    name = '李雷'
    gender = '男'

    def __init__(self):
        print("Father 构造函数运行")

    def speak_english(self):
        print("Father讲英语")


    def __juehuo(self):
        print("Father 的绝活")


class Mother:
    name = "韩梅梅"
    gender = "女"

    def __init__(self):
        print("Mother 构造函数运行")

    def speak_chinese(self):
        print("mother speak chinese")


class Child(Father, Mother):
    def __init__(self):
        print("child 构造函数运行")

    def speak_english(self):
        print("child speak english")

    def study(self):
        print("child study")


c = Child()
c.speak_english()
c.speak_chinese()
