# -*- coding: UTF-8 -*-

"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""

import time

myD = {'num1':'a', 'num2':'b', 'num3':'c'}
for key, value in dict.items(myD):
    print key,value
    time.sleep(2) #暂停一秒