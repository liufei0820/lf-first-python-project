#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 15:28
# @Author  : fei.liu

from threading import Thread, currentThread, RLock, Lock
import time

mutexA = mutexB = Lock()

class House(Thread):
    def run(self):
        self.room1()
        self.room2()

    def room1(self):
        mutexA.acquire()
        print(currentThread().name + "房间1拿到A锁")
        mutexB.acquire()
        print(currentThread().name + "房间1拿到B锁")
        mutexB.release()
        print(currentThread().name + "房间1释放A锁")
        mutexA.release()


    def room2(self):
        mutexB.acquire()
        print(currentThread().name + "房间2拿到B锁")
        time.sleep(1)
        mutexA.acquire()
        print(currentThread().name + "房间2拿到A锁")
        mutexA.release()
        print(currentThread().name + "房间2释放B锁")
        mutexB.release()


if __name__=='__main__':
    for i in range(10):
        t = House()
        t.start()

