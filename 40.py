# -*- coding: UTF-8 -*-

"""
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
"""

a = [1,4,6,9,13,16,19,28,40,100]
print "origin array:",a

nLen = len(a)
nDivLen = nLen / 2

for i in range(nDivLen):
        a[i],a[nLen-1-i] = a[nLen-1-i],a[i]
        
print "deverse array:",a




