# -*- coding: UTF-8 -*-

"""
题目：求100之内的素数。

程序分析：无。
"""

lower = int(raw_input("input the min num:"))
upper = int(raw_input("input the max num:"))

for num in range(lower,upper+1):
    if num > 1:
        bSuSu = True
        for i in range(2,num):
            if num % i == 0: 
                bSuSu = False
                break
        
        if bSuSu:
            print num