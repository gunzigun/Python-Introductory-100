# -*- coding: UTF-8 -*-

"""
题目：输入3个数a,b,c，按大小顺序输出。　　　

程序分析：无。

"""

if __name__ == "__main__":
    n1 = int(raw_input("please input num1:"))
    n2 = int(raw_input("please input num2:"))
    n3 = int(raw_input("please input num3:"))

    '''
    a = []
    a.append(n1)
    a.append(n2)
    a.append(n3)
    a.sort()
    print a
    '''

    def swap(a,b):
        return b,a

    if n1 > n2 : n1,n2 = swap(n1,n2)
    if n1 > n3 : n1,n3 = swap(n1,n3)
    if n2 > n3 : n2,n3 = swap(n2,n3)
    
    print n1,n2,n3
    
