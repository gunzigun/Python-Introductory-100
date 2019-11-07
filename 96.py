# -*- coding: UTF-8 -*-

"""
题目：计算字符串中子串出现的次数。

程序分析：无。
"""


if __name__ == "__main__":
    str1 = raw_input("please input a string:\n")
    str2 = raw_input("please input a sub string:\n")
    nCount = str1.count(str2)
    print nCount