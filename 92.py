# -*- coding: UTF-8 -*-

"""
题目：时间函数举例2。

程序分析：无。
"""


if __name__ == "__main__":
    import time
    start = time.time()
    for i in range(3000):
        print i
    end = time.time()

    print "pass time %0.3f second" % (end-start)