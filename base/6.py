#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: 数据类型

##################################
# Py3.X去除了long类型，现在只有一种整型——int，但它的行为就像2.X版本的long
# 新增了bytes类型，对应于2.X版本的八位串
# dict的.keys()、.items 和.values()方法返回迭代器，而之前的iterkeys()等函数都被废弃。同时去掉的还有 dict.has_key()，用 in替代它吧
##################################

#定义bytes
b = b'beijing'
print(b)
# str对象和bytes对象可以使用.encode() (str -> bytes) or .decode() (bytes -> str)方法相互转化。
c = b.decode()
print("bytes -> str:", c)
d = c.encode()
print("str -> bytes:", d)
