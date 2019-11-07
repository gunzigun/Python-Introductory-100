# -*- coding: UTF-8 -*-

"""
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

程序分析：无。
"""


if __name__ == "__main__":
    from sys import stdout
    
    filename = '.\\fuck.txt' #raw_input("please input file name:\n")
    fp = open(filename, "a")
    ch = raw_input("please input string:\n")
    while cmp(ch,"#") < 0:
        fp.write(ch)
        stdout.write(ch)
        ch = raw_input("")
    
    fp.close()