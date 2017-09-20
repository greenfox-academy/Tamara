from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def center_square(size):
    canvas.create_rectangle(150 - size, 150 - size, 150 + size, 150 + size, fill='red')

center_square(100)
center_square(70)
center_square(40)
root.mainloop()
