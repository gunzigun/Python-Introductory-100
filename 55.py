# -*- coding: UTF-8 -*-

"""
题目：学习使用按位取反~。

程序分析：~0=1; ~1=0; 
(1)先使a右移4位。 
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
(3)将上面二者进行&运算。

"""


if __name__ == "__main__":
        a = int(raw_input("input a num:"))
        print "a:",bin(a)
        b = ~a
        print "num1:",bin(b)
        a = ~b
        print "num2:",bin(a)


