# -*- coding: UTF-8 -*-

"""
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!
"""

def Jecheng(n):
    if n == 0:
        return 1
    return  n*Jecheng(n-1)

print Jecheng(5)
    


