from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def draw_nice_pic(step, color1, color2):
    for x in range(step, 299, step):
        canvas.create_line(x, 0, 300, x, fill=color1)
        canvas.create_line(0, x, x, 300, fill=color2)
    
draw_nice_pic(20, 'purple', 'green')


root.mainloop()
