from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.


size = 30
def checkerboard():
    for x in range(0, 300, 30):      
        for y in range(0, 300, 30):
            if ((x + y) / 30 % 2) == 0:
                color = 'black'
            else:
                color = 'white'            
            canvas.create_rectangle(x, y, size + x, size + y, fill=color)


checkerboard()
        

root.mainloop()
