#!/usr/bin/python3

__author__ = 'fei.liu'
__date__ = '16:42'


# str='Runoob'
#
# print(str)
# print(str[0:-1])
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str * 2)
# print(str + '你好')
#
# print('---------------------')
#
# print('hello\nrunoob')
# print(r'hello\nrunoob')

lowStr = "nihao"
print(lowStr.capitalize())
print(lowStr.center(3, ))

tabStr = "ni hao ma"
print(tabStr.expandtabs(100))

print(tabStr.find("hao", 1, 10))

digitStr = '123432'
mixStr = '123asf'
# print(digitStr.isalnum())
# print(digitStr.isalpha())
# print(digitStr.isdigit())
print(lowStr.isnumeric())
print(digitStr.isnumeric())
print(mixStr.isnumeric())

seq = ['hello', 'world', 'good', 'morning']
print(' '.join(seq))
print(', '.join(seq))

print(lowStr.center(40, '*'))