# -*- coding: UTF-8 -*-

"""
题目：八进制转换为十进制

程序分析：无。

"""

if __name__ == "__main__":
    n = 0
    p = raw_input("input a octal number:\n")
    for i in range(len(p)-1):
        n = n * 8 + (ord(p[i]) - ord("0"))

    print n

