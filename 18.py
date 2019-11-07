# -*- coding: UTF-8 -*-

"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
"""

a = int(raw_input("input a = "))
n = int(raw_input("input n = "))
Sn = []
Tn = a
for i in range(1,n+1):
    print Tn
    Sn.append(Tn)
    Tn = Tn * 10 + a

#lambda x,y : x + y,相当于add函数
#reduce (add,(1,2,3,4)),相当于(((1+2)+3)+4)
Sn = reduce(lambda x,y : x + y,Sn)
print 'the total num is:', Sn

