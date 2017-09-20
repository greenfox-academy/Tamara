from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

x = 0
y = 10
def purple_steps_squares(x, y):
    for i in range(1, 6):
        canvas.create_rectangle(x, x, y, y, fill='purple')
        x = 1.5 * x + 10 
        y = 1.5 * y + 10
    

purple_steps_squares(x, y)
root.mainloop()
