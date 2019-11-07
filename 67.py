# -*- coding: UTF-8 -*-

"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

程序分析：无。

"""
def inp(numbers,num):
    for i in range(num):
        numbers.append(int(raw_input('please input %dth num:'%(i+1))))
    print numbers


if __name__ == "__main__":
    array = []
    num = 6
    inp(array,num)

    minindex = 0
    for i in range(len(array)):
        minnum = array[minindex]
        nownum = array[i]
        if nownum < minnum:
            minindex = i
    print "minindex:",minindex
    array[len(array)-1],array[minindex] = array[minindex],array[len(array)-1]
    print array

    maxindex = 0
    for i in range(len(array)):
        maxnum = array[maxindex]
        nownum = array[i]
        if nownum > maxnum:
            maxindex = i
    print "maxindex:",maxindex
    array[0],array[maxindex] = array[maxindex],array[0]
    print array