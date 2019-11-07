# -*- coding: UTF-8 -*-

"""
题目：画图，学用line画直线。

程序分析：无。

"""
BeginX_Init = 150
BeginY_Init = 150
EndX_Init = 160 
EndY_Init = 160

if __name__ == "__main__":
        from Tkinter import *
        canvas = Canvas(width=300, height=300, bg='green')
        canvas.pack(expand=YES, fill=BOTH) 

        x0 = BeginX_Init
        y0 = BeginY_Init
        x1 = EndX_Init
        y1 = EndY_Init
        for i in range(19):
                canvas.create_line(x0,y0,x0,y1, width=2, fill='red')
                x0 -= 5
                y0 -= 5
                y1 += 5

        x0 = BeginX_Init
        y0 = BeginY_Init
        x1 = EndX_Init
        y1 = EndY_Init
        for i in range(21):
                canvas.create_line(x0,y0,x0,y1, width=2, fill='red')
                x0 += 5
                y0 += 5
                y1 += 5

        mainloop()