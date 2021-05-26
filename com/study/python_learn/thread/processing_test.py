#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 10:16
# @Author  : fei.liu
import os

# 导入线程
from threading import Thread

# 导入进程
from multiprocessing import Process


def work():
    print(os.getpid())

if __name__=='__main__':
    # 在主进程下开启多个线程
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print("主进程 ---->> 线程 PID", os.getpid())

    # 开启多个进程
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print("主进程 ---->> 进程 PID", os.getpid())
