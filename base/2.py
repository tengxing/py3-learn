#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: Python 2 有 ASCII str() 类型，unicode() 是单独的，不是 byte 类型。
#现在， 在 Python 3，我们最终有了 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。

name= '北京'
print(name)

#Python 2.x中,打印出来的是：\x88\xb1\xe5\x8c，u"北京"打印的是：\u5317\u4eac
#Python3.X 源码文件默认使用utf-8编码