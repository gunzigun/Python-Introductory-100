# -*- coding: UTF-8 -*-

"""
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。
"""

nJeCheng = 1
nSum = 0

for i in range(1,21):
    nJeCheng *= i 
    nSum += nJeCheng

print '1!+2!+...+n! = %d' % nSum
    


