from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

x = 0
x1 = 0
y = 30
y1 = 30
def checkerboard_white(x, x1, y, y1):
    for i in range(1, 10):
        if i % 2 == 0:
            canvas.create_rectangle(x, x1, y, y1, fill='black')
            x1 += 30
            y1 += 30
        else:
            canvas.create_rectangle(x, x1, y, y1, fill='white')            
            x1 += 30
            y1 += 30
def checkerboard_black(x, x1, y, y1):
    for i in range(1, 10):
        if i % 2 == 0:
            canvas.create_rectangle(x, x1, y, y1, fill='white')
            x1 += 30
            y1 += 30
        else:
            canvas.create_rectangle(x, x1, y, y1, fill='black')            
            x1 += 30
            y1 += 30

for j in range(1, 90):      
    if j % 2 == 0:
        checkerboard_black(x, x1, y, y1)
        x += 30
        y += 30
    else:
        checkerboard_white(x, x1, y, y1)
        x += 30
        y += 30  

root.mainloop()
