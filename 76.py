# -*- coding: UTF-8 -*-

"""
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n

程序分析：无。

"""

if __name__ == "__main__":
    n = int(raw_input("please input a num:"))
    
    nSum = 0
    while(n != 0):
        nSum += 1.0/n
        n -= 2

    print nSum
