# -*- coding: UTF-8 -*-

"""
题目：练习函数调用。
"""

def hello_world():
    print 'hello world'

def hello_worlds():
    for i in range(3):
        hello_world()
    
if __name__ == '__main__':
    hello_worlds()
