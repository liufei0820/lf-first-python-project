#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-07 21:39
# @Author  : fei.liu


f = open("/Users/apple/Documents/git-source/python-source/my-python-project/resources/foo.txt", "rb+")
# num = f.write("python 是一个非常好的语言。\n 是的，的确非常好!! \n")
#
# print(num)

# str = f.read()

# str = f.readline()

# str = f.readlines()
#
# print(str)

# for line in f:
#     print(line, end='')


# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)

b = f.write(b'0123456789abcdef')
print(b)

five = f.seek(5)
print(five)

one = f.read(1)
print(one)

three = f.seek(-3, 2)
print(three)

aa = f.read(1)
print(aa)


f.close()