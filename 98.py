# -*- coding: UTF-8 -*-

"""
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

程序分析：无。
"""


if __name__ == "__main__":
    from sys import stdout
    
    filename = '.\\test.txt' #raw_input("please input file name:\n")
    fp = open(filename, "w")
    ch = raw_input("please input string:\n")
    print "before upper:", ch
    ch = ch.upper()
    print "after upper:", ch
    fp.write(ch) 
    fp.close()