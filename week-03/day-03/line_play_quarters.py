from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
def line_in_the_middle():
    canvas.create_line(0, 150, 300, 150, fill='black')
    canvas.create_line(150, 0, 150, 300, fill='black')


def lines_in_quarters(start, width, color1, color2):
    half = int(width / 2)
    for x in range(start, half, 10):
        #q1
        canvas.create_line(x, start, half, x, fill=color1)
        canvas.create_line(start, x, x, half, fill=color2)
        #q2
        canvas.create_line(x+half, start, width, x, fill=color1)
        canvas.create_line(half, x, x+half, half, fill=color2)
        #q3
        canvas.create_line(x, half, half, x+half, fill=color1)
        canvas.create_line(start, x+half, x, width, fill=color2)
        #q4
        canvas.create_line(x+half, half, width, x+half, fill=color1)
        canvas.create_line(half, x+half, x+half, width, fill=color2)


line_in_the_middle()
lines_in_quarters(0, 300, 'purple', 'green')

root.mainloop()
