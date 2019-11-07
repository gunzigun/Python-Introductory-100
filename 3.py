#!/usr/bin/python1
# -*- coding: UTF-8 -*-

"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
x + 100 = n * n
x + 100 + 168 = m * m 
m*m-n*n = (m+n)*(m-n) = 168
m+n = i
m-n = j
i*j = 168
m = (i+j)/2
n = (i-j)/2
可知i和j都是偶数，i,j>=2
1<i<168/2+1
"""

for i in range (1,85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print x
