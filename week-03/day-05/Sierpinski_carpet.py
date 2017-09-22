from tkinter import *
import math
#import time
root = Tk()


canvas = Canvas(root, width='900', height='900', background='white')
canvas.pack()


def drawing_smaller_squeares(x, y, size):
    # time.sleep(0.01)
    # canvas.update()
    canvas.create_rectangle(x, y, x+size, y+size, outline='white', fill='black')


def draw_fractal(x, y, size):

    drawing_smaller_squeares(x, y, size)
    if size < 3:
        return
    else:
        draw_fractal(x, y, size/3)
        draw_fractal(x+ size/3, y, size/3)     
        draw_fractal(x+2*(size/3), y, size/3)
        draw_fractal(x+2*(size/3), y+size/3, size/3)
        draw_fractal(x+2*(size/3), y+2*(size/3), size/3)
        draw_fractal(x+size/3, y+2*(size/3), size/3)
        draw_fractal(x, y+2*(size/3), size/3)
        draw_fractal(x, y+size/3, size/3)
        

draw_fractal(0, 0, 400)

root.mainloop()