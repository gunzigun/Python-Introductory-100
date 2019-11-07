# -*- coding: UTF-8 -*-

"""
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

程序分析：无。

"""

def inp(numbers,num):
    for i in range(num):
        numbers.append(int(raw_input('please input %dth num:'%(i+1))))
    print numbers

#逆序函数
def reverse(numbers,left,right):
    nNum = right - left + 1
    nDiv = nNum/2 
    for i in range(nDiv):
        numbers[left+i],numbers[right-i] = numbers[right-i],numbers[left+i]
    print numbers


if __name__ == "__main__":
    
    num = int(raw_input("all num count:"))
    
    array = []
    inp(array,num)

    numMov = int(raw_input("mov num:"))

    nMovCount = num - numMov
    reverse(array,0,len(array)-1)
    reverse(array,0,numMov-1)
    reverse(array,numMov,len(array)-1)