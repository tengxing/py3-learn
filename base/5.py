#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: xrange

#range([start,] stop[, step])start与stop指定的范围以及step设定的步长，生成一个序列。
for i in range(1,101):
    print(i)
#xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。
#要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间。


# Python 3 中，range() 是像 xrange() 那样实现以至于一个专门的 xrange() 函数都不再存在（在 Python 3 中 xrange() 会抛出命名异常）,
#所以xrange在3中是不存在的，range默认的实现就是xrange