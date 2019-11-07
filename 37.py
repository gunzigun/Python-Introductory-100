# -*- coding: UTF-8 -*-

"""
题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，
选择一个最小的与第一个元素交换，下次类推，
即用第二个元素与后8个进行比较，并进行交换。
"""

N = 10
print "please in put 10 num:"
arrNum = []

for i in range(N):
    num = int(raw_input(("please input %dth num:" % (i+1))))
    arrNum.append(num)

print arrNum

for i in range(N-1):
    minIndex = i
    for j in range(i+1,N):
        if arrNum[j] < arrNum[minIndex]:
            minIndex = j
    arrNum[i],arrNum[minIndex] = arrNum[minIndex],arrNum[i]
    print "the %dth array:" % (i+1),arrNum




