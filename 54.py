# -*- coding: UTF-8 -*-

"""
题目：取一个整数a从右端开始的4〜7位。

程序分析：可以这样考虑： 
(1)先使a右移4位。 
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
(3)将上面二者进行&运算。

"""
beginbit = 4
endbit = 7

if __name__ == "__main__":
        a = int(raw_input("input a num:"))
        print bin(a)
        b = a >> (endbit-beginbit)
        print bin(b)
        print "(~0 << 4) is equal",bin(~0 << 4)
        print "~(~0 << 4) is equal",bin(~(~0 << 4))
        nMask = ~(~0 << 4)
        b &= nMask
        print bin(b)