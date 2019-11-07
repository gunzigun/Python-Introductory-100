# -*- coding: UTF-8 -*-

"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
"""

import string
s = raw_input('please input a string:\n')
nletter = 0
nspace = 0
ndigit = 0
nother = 0


def Function1():
    nletter = 0
    nspace = 0
    ndigit = 0
    nother = 0

    for c in s:
        if c.isalpha():
            nletter += 1
        elif c.isspace():
            nspace += 1
        elif c.isdigit():
            ndigit += 1
        else:
            nother += 1

    print 'char = %d,space = %d,digit = %d,others = %d' % (nletter,nspace,ndigit,nother)

def Function2():
    nletter = 0
    nspace = 0
    ndigit = 0
    nother = 0
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        if c.isalpha():
            nletter += 1
        elif c.isspace():
            nspace += 1
        elif c.isdigit():
            ndigit += 1
        else:
            nother += 1

    print 'char = %d,space = %d,digit = %d,others = %d' % (nletter,nspace,ndigit,nother)

Function1()
#Function2()