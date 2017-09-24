from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

def draw_nice_pic(step, width, color):
    half = int(width / 2)
    for x in range(step, half, step):
        canvas.create_line(x, half, half, half-x, fill=color)
        canvas.create_line(x, half, half, x+half, fill=color)
        canvas.create_line(half, x, x+half, half, fill=color)
        canvas.create_line(x+half, half, half, width-x, fill=color)
    
draw_nice_pic(10, 300, 'green')

root.mainloop()
