# -*- coding: UTF-8 -*-

"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
"""

latter = raw_input("Please the first letter:")

if "M" in latter:
    print "Monday"
elif "W" in latter:
    print "Wednesday"
elif "F" in latter:
    print "Friday"
elif "T" in latter:
    latter = raw_input("Please the second letter:")
    if "u" in latter:
        print "Tuesday"
    elif "h" in latter:
        print "Thursday"
elif "S" in latter:
    latter = raw_input("Please the second letter:")
    if "a" in latter:
        print "Saturday"
    elif "u" in latter:
        print "Sunday"
else:
    print "data error"

