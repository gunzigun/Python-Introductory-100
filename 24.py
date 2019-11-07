# -*- coding: UTF-8 -*-

"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律
"""

nNumCount = 20

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) 

nSum = 0.0
for i in range(1,nNumCount+1):
    fenzi = fibonacci(i+2)
    fenmu = fibonacci(i+1)
    nSum += (fenzi*1.0)/fenmu

print nSum

    


