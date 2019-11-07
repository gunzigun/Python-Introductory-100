# -*- coding: UTF-8 -*-

"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析：关键是计算出每一项的值。
"""

def LenReturn(n):
    nNum = 100.0
    for i in range(1,n+1):
        nNum = nNum / 2 * (i / i)
    return nNum

def LenOnFloorReturn(n):
    return LenReturn(n-1)+LenReturn(n)

def PassLenth(n):
    nSum = 0
    for i in range(1,n+1):
        nSum = nSum + LenOnFloorReturn(i)

    return nSum - LenReturn(n)

print "10th pass hight:",PassLenth(10)
print "10th return hight:", LenReturn(10)


