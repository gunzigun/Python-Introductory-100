#!/usr/bin/python1
# -*- coding: UTF-8 -*-

"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
"""

def GetLevelPro(nNum, nRate):
    nCount = nNum * nRate
    print nCount
    return nCount


i = int(raw_input('净利润:'))
arrLim = [1000000,600000,400000,200000,100000,0]
arrRate = [0.01,0.015,0.03,0.05,0.075,0.1]

#总提成数目
r = 0
for k in range(0,len(arrLim)):
    if i > arrLim[k]:
        r = r + GetLevelPro(i-arrLim[k],arrRate[k])
        i = arrLim[k]
        
print r