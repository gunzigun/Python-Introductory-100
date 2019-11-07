# -*- coding: UTF-8 -*-

"""
题目：学习使用auto定义变量的用法。

程序分析：没有auto关键字，使用变量作用域来举例吧

"""

num = 2
def autofunction():
        num = 1
        print "autofunction num:", num
        num +=1

for i in range(3):
        print "range num:",num
        autofunction()
        num += 1