# -*- coding: UTF-8 -*-

"""
题目：暂停一秒输出，并格式化当前时间
"""

import time

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print time.localtime(time.time())
print ("%d" % time.localtime(time.time()).tm_mon)

time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))