# -*- coding: UTF-8 -*-

"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。
"""

nNum = int(raw_input("please input a num less than 99999:\n"))
nCount = 0
while nNum != 0:
    nLeft = nNum % 10
    nNum = int(nNum / 10)
    
    print nLeft,
    nCount += 1

print "\nit a %d count number " % nCount