#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-03 19:52
# @Author  : fei.liu

def reverseWords(input):
    #通过空格将字符串分隔符，将各个单词分隔为列表
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]

    output = " ".join(inputWords)
    return output

if __name__ == "__main__":
    input = 'i like runoob'
    rw = reverseWords(input)
    print(rw)


