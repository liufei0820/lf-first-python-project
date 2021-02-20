#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-22 09:52
# @Author  : fei.liu

def read_file1():
    f = open("exception_demo.py", encoding="utf8")
    while True:
        z = f.read(10)
        print(z)
        if z is "":
            break

    f.close()

# read_file1()


# with open 帮我们自动关闭文件的输入输出流
def read_file2(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
        print(lines)

# read_file2("exception_demo.py")


def write_file(filename: str):
    with open(filename, "w", encoding="utf8") as f:
        for i in range(100):
            f.write(str(i))
            f.flush()


write_file("../../../resources/11.txt")

