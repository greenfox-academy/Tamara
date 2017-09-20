from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

def four_rectangles():
    blue_box = canvas.create_rectangle(120, 120, 170, 170, fill='blue')
    red_box = canvas.create_rectangle(90, 90, 100, 100, fill='red')
    orange_box = canvas.create_rectangle(200, 150, 150, 190, fill='orange')
    green_box = canvas.create_rectangle(80, 40, 40, 90, fill='green')


four_rectangles()
root.mainloop()
