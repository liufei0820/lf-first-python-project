#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-24 15:37
# @Author  : fei.liu


from abc import ABCMeta, abstractmethod


class Tester(metaclass=ABCMeta):

    @abstractmethod
    def test(self):
        pass


class FunctionTester(Tester):
    def test(self):
        print("功能测试")


f = FunctionTester()
