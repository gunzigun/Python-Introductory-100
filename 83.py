# -*- coding: UTF-8 -*-

"""
题目：求0—7所能组成的奇数个数。

程序分析：

组成1位数是4个。

组成2位数是7*4个。

组成3位数是7*8*4个。

组成4位数是7*8*8*4个。

程序分析：无
"""

def numcout(nBit):
    num = 0
    nBitleft = nBit - 1
    
    if nBitleft == 0:
        num = 4
    else:
        num = 7 * 4
        for i in range(nBitleft-1):
            num *= 8
    
    return num


if __name__ == "__main__":
    nMaxBit = int(raw_input("please input the max num bit:"))
    
    sum = 0
    for i in range(nMaxBit):
        sum += numcout(i+1)
        print sum