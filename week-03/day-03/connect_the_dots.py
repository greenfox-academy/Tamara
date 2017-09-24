from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

lines1 = [[10, 10], [290,  10], [290, 290], [10, 290]]
lines2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

def connecting_dots(lines):
    for point1 in lines:
        for point2 in lines:
            canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill='green')


connect_dots_in_order(lines1)
connect_dots_in_order(lines2)


#in order
def connect_dots_in_order(lines):
    x = 0
    y = 1
    length = len(lines)-1
    for i in range(length):
        canvas.create_line(lines[i][x], lines[i][y], lines[i+1][x], lines[i+1][y], fill='green')
    canvas.create_line(lines[length][x], lines[length][y], lines[0][x], lines[0][y], fill='green')


connect_dots_in_order(lines1)
connect_dots_in_order(lines2)

root.mainloop()
