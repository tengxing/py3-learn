#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: 迭代

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
l = ['g','t','t','o']
result = iter(l)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# 其实可以简单的使用如下遍历
for i in l:
    print(i)

# 生成器yield
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值
def fibonacci(): # 生成器函数 - 斐波那契
    while True:
        a=1
        yield a
        a+=1
tmp = fibonacci()
for i in range(1,11):
    print(fibonacci())


'''
什么情况下需要使用 yield？
一个函数 f，f 返回一个 list，这个 list 是动态计算出来的
（不管是数学上的计算还是逻辑上的读取格式化），并且这个 list
 会很大（无论是固定很大还是随着输入参数的增大而增大），这个时候，
 我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到
 每个 list 元素而不是直接得到一个完整的 list 来节省内存，这个时
 候 yield 就很有用。
'''

