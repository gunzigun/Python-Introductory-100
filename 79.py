# -*- coding: UTF-8 -*-

"""
题目：字符串排序。

程序分析：无。
"""

if __name__ == "__main__":
    
    str1 = raw_input('input string1:\n')
    str2 = raw_input('input string2:\n')
    str3 = raw_input('input string3:\n')
    print str1
    print str2
    print str3
    
    if str1 > str2 : str1,str2 = str2,str1
    if str1 > str3 : str1,str3 = str3,str1
    if str2 > str3 : str2,str3 = str3,str2
 
    print 'after being sorted.'
    print str1
    print str2
    print str3
