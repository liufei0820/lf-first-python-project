#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 10:35
# @Author  : fei.liu

from sympy import *
from sympy.abc import a,b,c,d,x,y,z


x = Symbol('x')
f = (1+2*x)*x**2
ff = expand(f)
print("expand")
print(ff)

print("factor")
f = x**2+1+2*x
ff = factor(f)
print(ff)

print("simplify")
print(simplify((x**3 + x**2 -x -1)/(x**2 + x*2 +1)))

print("trigsimp")
print(trigsimp(sin(x)/cos(x)))

print("powsimp")
print(powsimp(x**a*x**b))

print("apart")
f = (x+2)/(x+1)
ff = apart(f)
print(ff)


print("as_coeff_add")
tmp = 1 + 3 + x + 3*y + x**y + 2*x
u,v = tmp.as_coeff_add()
print(u)
print(v)
print(zoo)
res = [u]
for i in v:
    res.append(i)

print(res)

def demoninator_has_add(monomial):
    for e in monomial.args:
        if (isinstance(e, Pow) and e.exp == -1):
            return True
    return False

for i in res:

    print("需要判断的数据：%".format(i))
    if demoninator_has_add(i):
        print("分母包含加减：", i)


r1 = ratsimp((x + y**2)/ (x + y) + y / (x - 1 + y))
u1, v1 = r1.as_coeff_add()
print(u1)
print(v1)







