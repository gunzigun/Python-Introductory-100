# -*- coding: UTF-8 -*-

"""
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""

from sys import stdout

nMaxlevel = 4

def getLevelNum(n):
    return 2*(nMaxlevel-n)+1 

def getLineNum(line):
    nLevel = abs(line-nMaxlevel)+1
    return getLevelNum(nLevel)

nMaxStarNum = getLevelNum(1)
for i in range(1,2*nMaxlevel):
    nStartNum = getLineNum(i)
    nSpaceNum = (nMaxStarNum - nStartNum)/2

    for j in range(1,nSpaceNum+1):
        print " ",
    
    for k in range(1,nStartNum+1):
        print "*",

    print 










