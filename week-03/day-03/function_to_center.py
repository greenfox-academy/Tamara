from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def lines_to_the_center(x, y):
    canvas.create_line(x, y, 150, 150, fill='red')

fix_point = [0, 300]
for x in range(0, 301, 20):
    for y in fix_point:
        lines_to_the_center(y, x)
        lines_to_the_center(x, y)


root.mainloop()
