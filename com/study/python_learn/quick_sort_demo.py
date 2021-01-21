#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-20 14:31
# @Author  : fei.liu

def quick_sort(list, low, high):
    if low > high:
        return
    i = low
    j = high
    temp = list[low]

    while i < j:
        while (temp <= list[j]) and (i < j):
            j = j - 1

        while (temp >= list[i]) and (i < j):
            i = i + 1

        if i < j:
            list[i], list[j] = list[j], list[i]

        list[low], list[i] = list[i], list[low]

        quick_sort(list, low, j - 1)
        quick_sort(list, j + 1, high)


if __name__ == '__main__':
    list = [10, 7, 2, 4, 7, 62, 3, 4, 2, 1, 8, 9, 19]
    print(len(list))
    quick_sort(list, 0, len(list) - 1)
    for v in list:
        print(v)

