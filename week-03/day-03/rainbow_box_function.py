from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

rainbow = ('red', 'orange', 'yellow', 'green','blue','indigo','violet')
def rainbow_squares (size, color):
    canvas.create_rectangle(150 - size, 150 - size, 150 + size, 150 + size, 
                                       fill=color)
        
size = 150
for i in rainbow:
    rainbow_squares(size, i)
    size -= 20

root.mainloop()
