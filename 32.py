# -*- coding: UTF-8 -*-

"""
题目：按相反的顺序输出列表的值。

程序分析：无。
"""

arr = ["a","b","c"]

for i in arr[::-1]:
    print i


nLenth = len(arr)
for i in range(nLenth):
    print arr[nLenth-i-1]