# -*- coding: UTF-8 -*-

"""
题目：学习使用按位或 | 。

程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1

"""

if __name__ == '__main__':
        a = 077
        b = a | 3
        print a 
        print b
        b |= 7
        print b 