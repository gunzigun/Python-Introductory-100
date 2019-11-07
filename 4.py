#!/usr/bin/python1
# -*- coding: UTF-8 -*-

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

monthday = [0,31,28,31,30,31,30,31,31,30,31,30]

nSum = 0
for index in range(month):
    nSum += monthday[index]

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) and month > 2):
    nSum += 1
    
print "\nthis is the", nSum+day, "th day"