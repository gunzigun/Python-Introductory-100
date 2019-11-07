#!/usr/bin/python1
# -*- coding: UTF-8 -*-

"""
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），
又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
"""
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2) 
    
print fibonacci(6)