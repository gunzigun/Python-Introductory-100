# -*- coding: UTF-8 -*-

"""
题目：使用lambda来创建匿名函数。

程序分析：无

"""

MAX_NUM = lambda x,y : (x>y)*x+(x<y)*y
MIN_NUM = lambda x,y : (x>y)*y+(x<y)*x

if __name__ == '__main__':
        a = 10
        b = 20 
        print "max num is %d" % MAX_NUM(a,b)
        print "min num is %d" % MIN_NUM(a,b)