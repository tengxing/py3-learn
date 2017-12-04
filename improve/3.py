#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: 面向对象之类继承


class People:
    name = ''
    age = 0

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

class Singer:
    name = ''
    hobby = ""

    def __init__(self, n, a):
        self.name = n
        self.hobby = a

    def speak(self):
        print("%s 说: 我的爱好是 %s 。" % (self.name, self.hobby))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, g):
        # 调用父类的构函
        People.__init__(self, n, a)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = Student('ken', 10,  3)
s.speak()

# 多继承示例
class Student(People,Singer):
    grade = ''

    def __init__(self, n, a, h, g):
        # 调用父类的构函
        People.__init__(self, n, a)
        Singer.__init__(self, n, h)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了,我的爱好是 %s,我在读 %d 年级 。" % (self.name, self.age, self.hobby,self.grade))
s = Student('ken', 10, "唱歌", 3)
s.speak()