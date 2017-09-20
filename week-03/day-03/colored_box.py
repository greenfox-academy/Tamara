from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
lime_box = canvas.create_rectangle(50, 50, 100, 100, outline='red', fill='lime green')

red_line = canvas.create_line(120, 120, 120, 50, fill='red')
blue_line = canvas.create_line(120, 50, 200, 50, fill='blue')
green_line = canvas.create_line(200, 50, 200, 120, fill='green')
black_line = canvas.create_line(120, 120, 200, 120, fill='black')




root.mainloop()
