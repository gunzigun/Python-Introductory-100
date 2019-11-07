# -*- coding: UTF-8 -*-

"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""

from math import sqrt

nAllNum = 0
for num in range(101,201):
    nNumqrt = int(sqrt(num+1))
    isSu = True 
    for i in range(2,nNumqrt+1):
        if num % i == 0:
            isSu = False
            break

    if isSu:
        nAllNum += 1
        print num
        if nAllNum % 10 == 0:
            print ''

print 'The total is %d' %  nAllNum
 