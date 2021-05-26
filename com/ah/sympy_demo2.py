#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 15:10
# @Author  : fei.liu

import sys
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


def get_reciprocal(i):                          # 取倒数
    r = Pow(i, -1)
    return r


if __name__ == "__main__":
    # print(sys.argv[1])
    # print("asdfsf")
    # poly, *variable = eval(sys.argv[1])
    # poly, *variable = eval("(x + y**2)/(x + y)+y/(x - 1 + y) + x*2,x,y")
    poly, *variable = eval("x + y**2+y + x*2,x,y")
    math_expression = fraction(radsimp(poly))
    # 分子
    print("numerator {}".format(math_expression[0]))
    # 分母
    print("denominator {}".format(math_expression[1]))




