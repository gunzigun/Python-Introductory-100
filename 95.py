# -*- coding: UTF-8 -*-

"""
题目：字符串日期转换为易读的日期格式。

程序分析：无。
"""


if __name__ == "__main__":
    from dateutil import parser
    dt = parser.parse("Aug 28 2015 11:00PM")
    print dt