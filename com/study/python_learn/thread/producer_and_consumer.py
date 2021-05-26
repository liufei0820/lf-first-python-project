#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 15:53
# @Author  : fei.liu

import threading
import time

condition = threading.Condition()
products = 0

class Producer(threading.Thread):

    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products <= 10:
                    products += 1
                    print("{}:{} 库存不足，商品数量小于等于0，现在商品总数量是{}".format("生产者", threading.currentThread().getName(), products))
                    condition.notify()

                else:
                    print("{}:{} 库存充足，商品数量大于10，现在商品总数量是{}".format("生产者", threading.currentThread().getName(), products))
                    condition.wait()

                condition.release()
                time.sleep(2)



class Consumer(threading.Thread):
    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products >= 1:
                    products -= 1
                    print("{}:{} 我消费了一件商品，现在商品总数量是{}".format("消费者", threading.currentThread().getName(), products))
                else:
                    print("{}:{} 没有库存，停止消费{}".format("消费者", threading.currentThread().getName(), products))
                    condition.wait()

                condition.release()
                time.sleep(2)


if __name__ == '__main__':
    for i in range(3):
        p = Producer()
        p.start()


    for i in range(10):
        c = Consumer()
        c.start()





