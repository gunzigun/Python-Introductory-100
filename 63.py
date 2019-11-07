# -*- coding: UTF-8 -*-

"""
题目：画椭圆。　

程序分析：使用 Tkinter。

"""

if __name__ == "__main__":
        from Tkinter import *
        canvas = Canvas(width = 400,height = 600,bg = 'white')

        x0 = 100
        y0 = 200
        x1 = 300
        y1 = 400
        nAdd = 5
        canvas.create_oval(x0,y0,x1,y1)
        
        for i in range(21):
                canvas.create_oval(x0,y0,x1,y1)
                x0 += nAdd
                x1 -= nAdd
                y0 -= nAdd
                y1 += nAdd

        canvas.pack()
        mainloop()