# -*- coding: UTF-8 -*-

"""
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

程序分析：999999 / 13 = 76923。
"""

if __name__ == "__main__":
    zi = int(raw_input("please input a odd num:\n"))
    
    bFind = False
    nCount = 1
    num = 9

    while bFind != True:
        if num % zi == 0:
            bFind = True
        else:
            num *= 10
            num += 9
            nCount += 1

    print "%d * 9 can div by %d" % (nCount, zi)
    print "%d / %d = %d" % (num, zi, num/zi)