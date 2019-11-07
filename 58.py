# -*- coding: UTF-8 -*-

"""
题目：画图，学用rectangle画方形。　　　

程序分析：

"""
BeginX_Init = 263
BeginY_Init = 263
EndX_Init = 275 
EndY_Init = 275

if __name__ == "__main__":
        from Tkinter import *
        root = Tk()
        root.title('Canvas')
        canvas = Canvas(root, width=400, height=400, bg='yellow')
        canvas.pack(expand=YES, fill=BOTH) 

        x0 = BeginX_Init
        y0 = BeginY_Init
        x1 = EndX_Init
        y1 = EndY_Init
        for i in range(19):
                canvas.create_rectangle(x0, y0, x1, y1)
                x0 -= 5
                y0 -= 5
                x1 += 5
                y1 += 5
        
        canvas.pack()
        mainloop()