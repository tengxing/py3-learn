#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: 异常

#捕获异常的语法由 except exc, var 改为 except exc as var
import sys

# 自定义Error
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    f = open('data/tmp.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise #唯一的一个参数指定了要被抛出的异常


#测试自定义异常
try:
    raise MyError(2/1)
except MyError as myError:
    print('My exception occurred, value:', myError.value)

