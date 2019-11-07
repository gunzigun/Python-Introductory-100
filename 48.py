# -*- coding: UTF-8 -*-

"""
题目：数字比较。

程序分析：无

"""
if __name__ == '__main__':
        A = int(raw_input("please input A:"))
        B = int(raw_input("please input B:"))

        if A > B:
                print "%d > %d" % (A,B)
        elif A == B:
                print "%d = %d" % (A,B)
        elif A < B:
                print "%d < %d" % (A,B)
        else:
                print "unknow"