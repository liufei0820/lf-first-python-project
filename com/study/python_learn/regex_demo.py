#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-01-19 14:48
# @Author  : fei.liu

'''
正则表达式是用来操作字符串的一种逻辑公式
'''

import re

s = "百度http://www.baidu.com"
reg = "http://[w]{3}\.[a-z0-9]*\.com"
result = re.findall(reg, s)

# print(result)

# 元字符
'''
.       代表的是换行符以外的任意的字符  \r\n
\w      匹配字符或数字或下划线或汉子
\s      匹配任意的空白符
\d      匹配任意的数字 0-9
^       匹配字符串的开始
$       匹配字符串的结束

*       代码的是前面正则表达式重复0次或多次
+       代码的是前面正则表达式重复1次或多次
?       代码的是前面正则表达式重复0次或1次
{n}     代码的是前面正则表达式重复n次
{n,}    代码的是前面正则表达式重复最少n次
{n,m}   代码的是前面正则表达式重复n次到m次
'''

# 分组匹配
s = "我的qq号码是:324235234, 我的邮编是:100000"
reg = "(\d{9}).*(\d{6})"
print(re.search(reg, s).group(0))
print(re.search(reg, s).group(1))
print(re.search(reg, s).group(2))
# print(re.search(reg, s).group(3))


'''
正则表达式的高级应用
贪婪与懒惰   贪婪与非贪婪
非贪婪：尽可能少的匹配
非贪婪操作符 ?
这个非贪婪操作符可以使用在 * + ? 后边
* 重复0次或者多次  *?
+ 重复1次或者多次  +?
? 重复0次或者1次   ??
'''
s = "baiduuuuuuuuu"
reg = "baidu+?"
print(re.findall(reg, s))

'''
分之条件匹配
操作符     |
'''
s = "我的电话好吗：010-89888888 0431-32442542 0432-4358345"
reg = "0\d{2}-\d{8}|0\d{3}-\d{7,8}"
print(re.findall(reg, s))


'''
零宽断言
(?=reg)     匹配reg前边的位置
(?<=reg)    匹配reg后边的位置
(?!=reg)    匹配后面跟的不是reg的位置
(?<!reg)    匹配前边跟的不是reg的位置
'''













