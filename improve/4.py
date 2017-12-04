#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Mail: tengxing7452@163.com
# Author: StarryTeng
# Description: json处理

import json

# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。
# 不用当心Ture,None等等,会自动编码，解码true,null
data = {
    'name': 'tengxing',
    'url': 'http://www.yjxxclub.com',
    'job': 'programer'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)