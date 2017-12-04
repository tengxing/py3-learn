#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: 面向对象之类构造器


class Computations:
    num1 = 0
    num2 = 0
    __pi = 3.1415

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        return self.num1+self.num2

    def minus(self):
        return self.num1-self.num2

    def mul(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2


result = Computations(1, 2)
print(result.plus())
print(result.minus())
print(result.mul())
print(result.divide())
#print(result.pi) 私有变量无法直接访问


# 类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法
