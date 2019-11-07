# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
"""

for i in range(100,1000):
    nTemp = i

    x = nTemp / 100
    nTemp = nTemp % 100

    y = nTemp / 10
    nTemp = nTemp % 10

    z = nTemp

    #nSum = x*x*x + y*y*y + z*z*z
    nSum = x**3 + y**3 + z**3

    if nSum == i:
        b =  ("%d是水仙花数：%d = %d三次方 + %d三次方 + %d三次方" % (i,i,x,y,z))
        print b.decode('utf-8').encode('cp936') 
        #print "%d是水仙花数：%d = %d三次方 + %d三次方 + %d三次方" % (i,i,x,y,z)