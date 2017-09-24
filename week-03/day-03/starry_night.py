from tkinter import *
from random import *

root = Tk()


canvas = Canvas(root, width='300', height='300', background="black")
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

def night_sky(N):
    for x in range(N):
        x = randint(5, 300)
        y = randint(5, 300)
        color = choice(['lightgrey', 'grey', 'silver', 'lightslategrey'])
        canvas.create_rectangle(x, y, x+5, y+5, fill=color)
    

night_sky(100)

root.mainloop()
