# -*- coding: UTF-8 -*-

"""
题目：反向输出一个链表。

程序分析：无。

"""

if __name__ == "__main__":
    l = [int(raw_input("please input %dth num:"%(i+1))) for i in range(5)]
    
    l.reverse()

    print l