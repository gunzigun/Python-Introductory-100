# -*- coding: UTF-8 -*-

"""
题目：列表使用实例。

程序分析：无。
"""

testlist = [10086, "china mobile", [1,2,4,5]]

print len(testlist)
print testlist[1:]

testlist.append("I\'m new here!")

print len(testlist)
print testlist[-1]

print testlist.pop(1)
print len(testlist)
print testlist

matrix = [[1, 2, 3],  
[4, 5, 6],  
[7, 8, 9]]  
print matrix  
print matrix[1]  
col2 = [row[1] for row in matrix]#get a  column from a matrix  
print col2  
col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item  
print col2even