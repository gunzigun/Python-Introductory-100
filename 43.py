# -*- coding: UTF-8 -*-

"""
题目：模仿静态变量(static)另一案例。

程序分析：演示一个python作用域使用方法

"""

class Num:
        num = 1
        def inc(self):
                self.num += 1
                print "num is %d" % self.num

nNum = 2
inst = Num()
for i in range(3):
        nNum += 1
        print "the out num is %d" % nNum
        inst.inc()