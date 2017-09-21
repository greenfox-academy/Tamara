from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

# fill the canvas with a checkerboard pattern.


def yellow_square(x, y, a):
    line = canvas.create_line(x, y+a/3, x+a, y+a/3, fill='red')
    line = canvas.create_line(x, y+2*a/3, x+a, y+2*a/3, fill='red')
    line = canvas.create_line(x+a/3, y, x+a/3, y+a, fill='red')
    line = canvas.create_line(x+2*a/3, y, x+2*a/3, y+a, fill='red')
    if a < 13:
        return
    else:
        return yellow_square(x+a/3, y, a/3), yellow_square(x, y+a/3, a/3), yellow_square(x+a/3, y+2*a/3, a/3), yellow_square(x+2*a/3, y+a/3, a/3)

box = canvas.create_rectangle(0, 0, 600, 600, fill='yellow')           

yellow_square(0, 0, 600)
        

root.mainloop()