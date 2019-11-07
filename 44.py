# -*- coding: UTF-8 -*-

"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
程序分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。

"""

import numpy as np

arrayX = np.array([[12,7,3],[4,5,6],[7,8,9]])
arrayY = np.array([[5,8,1],[6,7,3],[4,5,9]])

arrayNew = arrayX + arrayY

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
 
# 迭代输出行
for i in range(len(arrayX)):
   # 迭代输出列
   for j in range(len(arrayX[0])):
       result[i][j] = arrayX[i][j] + arrayX[i][j]
 
print result


arrNP = np.array([1,2,3]).reshape(1,3)
print arrNP

arrNP = arrNP.reshape(3,1)
print arrNP