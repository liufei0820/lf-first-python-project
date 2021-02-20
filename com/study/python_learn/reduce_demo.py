#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-21 18:57
# @Author  : fei.liu

# 列表推导式： x for x in a

y = [x + 1 for x in [1, 2, 3, 4]]
# print(y)

# print(list(x + 1 for x in [1, 2, 3, 4] if x > 2))


# 集合推导式：
y = {x + 1 for x in [1, 2, 3, 4]}
# print(y)


# 字典推导式
d = {x: y for x, y in {"a":1, "b":2}.items()}
print(d)

