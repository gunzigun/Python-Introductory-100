# -*- coding: UTF-8 -*-

"""
题目：画图，学用circle画圆形。　　　

程序分析：无

"""


if __name__ == "__main__":
        from Tkinter import *
        
        canvas = Canvas(width=400, height=400, bg='yellow')
        canvas.pack(expand=YES, fill=BOTH)   
        k = 1
        for i in range(0,26):
                canvas.create_oval(200 - k,200 - k,200 + k,200 + k, width=1)
                k += 7
        
        mainloop()