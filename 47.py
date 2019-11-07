# -*- coding: UTF-8 -*-

"""
题目：两个变量值互换。

程序分析：无

"""
def exchange(a,b):
        a,b = b,a
        return (a,b)

"""
if __name__ == '__main__':
    x = 10
    y = 20
    print 'x = %d,y = %d' % (x,y)
    x,y = exchange(x,y)
    print 'x = %d,y = %d' % (x,y)
"""


A = int(raw_input("please input A:"))
B = int(raw_input("please input B:"))

print "before exchange: %s, %s" % (A, B)

A,B = B,A #exchange(A,B)

print "after exchange: %s, %s" % (A, B)