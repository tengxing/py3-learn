#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: 除法运算

import math

#Python中的除法较其它语言显得非常高端，有套很复杂的规则。Python中的除法有两个运算符，/和//

print(1/2)#0.5而不是0，在2.x中为0，很人性化
print(-1//3)#floor除法，会对除法的结果自动进行一个floor操作,py2或py3不变
print(math.trunc(-1/9))#数字的小数部分去掉,只保留整数部分