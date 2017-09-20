from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def horizontal_lines_drawing(x, y):
    blue_line = canvas.create_line(x, y, 50, 50, fill='blue')
    red_line = canvas.create_line(x, y, 50, 40, fill='red')
    green_line = canvas.create_line(x, y, 50, 60, fill='green')


horizontal_lines_drawing(0, 50)

root.mainloop()
