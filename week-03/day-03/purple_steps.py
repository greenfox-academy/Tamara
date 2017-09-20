from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

x = 0
y = 10
def purple_steps_squares(x, y):
    for i in range(1, 15):
        canvas.create_rectangle(x, x, y, y, fill='purple')
        x += 10 
        y += 10
    

purple_steps_squares(x, y)
root.mainloop()
