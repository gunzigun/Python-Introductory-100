# -*- coding: UTF-8 -*-

"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

"""

a = [1,4,6,9,13,16,19,28,40,100,0]
a.sort()
print a

num = int(raw_input("please input a num:"))
a.append(num)

k = 0
for i in range(len(a)-1):
    if num < a[i]:
        k = i
        break


for i in range(len(a)-1,k,-1):
    a[i] = a[i-1]
    print a

a[k] = num
print a


