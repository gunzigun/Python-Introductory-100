# -*- coding: UTF-8 -*-

"""
题目：按逗号分隔列表。
"""

arr = [1,2,3,4,5]
s = ",".join(str(n) for n in arr)
print s

arr1 = ["a","b","c","d"]
s1 = ";".join(s for s in arr1)
print s1
