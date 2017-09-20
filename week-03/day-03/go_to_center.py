from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def three_lines_drawing(x, y):
    green_line = canvas.create_line(x, y, 150, 150, fill='green')
    red_line = canvas.create_line(x, y, 140, 120, fill='red')
    red_line = canvas.create_line(x, y, 140, 170, fill='red')



three_lines_drawing(0, 0)
root.mainloop()
