# -*- coding: UTF-8 -*-

"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。
"""

nNum = int(raw_input("please input a 5 bit num:\n"))
str = str(nNum)

nLenthDiv = len(str)

bFlag = True
for i in range(nLenthDiv/2):
    if str[i] != str[nLenthDiv-1-i]:
        bFlag = False
        break

if bFlag:
    print "%d is a back num!" % nNum
else:
    print "%d not a back num!" % nNum
