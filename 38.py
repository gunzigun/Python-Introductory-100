# -*- coding: UTF-8 -*-

"""
题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
"""

import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

sum = array[0][0] + array[1][1] + array[2][2]
 
print sum