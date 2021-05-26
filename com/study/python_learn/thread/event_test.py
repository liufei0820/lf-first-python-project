#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 10:21
# @Author  : fei.liu

# 事件
'''
线程间通信
'''

import threading, time

class Boss(threading.Thread):
    def run(self):
        print("BOSS: 从现在开始就要996了，欢呼吧")
        # 事件设置
        print(event.isSet())
        event.set()
        time.sleep(3)
        print("BOSS: 大家干完了，不996了")
        print(event.isSet())
        event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker: 命苦")
        event.clear()
        event.wait()
        print("Worker: oh yeah!!!")


if __name__=="__main__":
    event = threading.Event()

    threads = []
    for i in range(5):
        threads.append(Worker())

    threads.append(Boss())

    for t in threads:
        t.start()
