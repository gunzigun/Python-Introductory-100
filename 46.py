# -*- coding: UTF-8 -*-

"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。

程序分析：无

"""

bAgain = True

while bAgain:
        nNum = int(raw_input("please input a num:"))
        nSq = nNum * nNum 
        print "the out put:%d" % nSq
        if nSq < 50:
                bAgain = False