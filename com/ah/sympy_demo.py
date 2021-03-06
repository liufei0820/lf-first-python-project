#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-03-01 20:03
# @Author  : fei.liu


from sympy import *
from sympy.abc import a,b,c,d,x,y,z
def process(mul_poly, *variable):               # 化解分裂多项式，返回单项式数组
    tmp = simplify(mul_poly)                    # 多项式化简
    if len(variable) > 1 or tmp.has(zoo):
        tmp = expand(apart(tmp, variable[0]))   # apart 分裂项式，expand多项式展开
    else:
        tmp = expand(apart(tmp))

    u, v = tmp.as_coeff_add()
    res = [u]
    for i in v:
        if i.has(zoo):
            return
        res.append(i)
    return res


def demoninator_has_add(monomial):              # 判断单项式的分母是否包含加减法
    for e in monomial.args:
        if (isinstance(e, Pow) and e.exp == -1):
            return True
    return False


def get_reciprocal(i):                          # 取倒数
    r = Pow(i, -1)
    return r


# try:
#     poly, *variable = eval(input("输入："))
#     monomial = process(poly, *variable)
#     if monomial is not None:
#         print("拆分后的单项式：", monomial)
#         for i in monomial:
#             if demoninator_has_add(i):
#                 print("分母包含加减：", i)
#     else:
#         print("divide by zero!")
# except ZeroDivisionError:
#     print("divide by zero!")

try:
    poly, *variable = eval(input("输入："))
    print(fraction(radsimp(poly)))
    print("---------")
    for i in fraction(radsimp(poly)):
        print(i)
        print(process(i, *variable))
        print("---------")
except ZeroDivisionError:
    print("divide by zero")