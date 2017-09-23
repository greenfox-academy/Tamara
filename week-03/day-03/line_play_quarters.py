from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
def line_in_the_middle():
    canvas.create_line(0, 150, 300, 150, fill='black')
    canvas.create_line(150, 0, 150, 300, fill='black')


def draw_nice_pic(step, start, end, color1, color2):
    for x in range(start, end, step):
        canvas.create_line(x, start, end, x, fill=color1)
        canvas.create_line(start, x, x, end, fill=color2)
color1='purple'
color2='green'
#q1
for x in range(0, 150, 10):
        canvas.create_line(x, 0, 150, x, fill=color1)
        canvas.create_line(0, x, x, 150, fill=color2)
#q2
for x in range(0, 150, 10):
        canvas.create_line(x+150, 0, 300, x, fill=color1)
        canvas.create_line(150, x, x+150, 150, fill=color2)

#q3
for x in range(0, 150, 10):
        canvas.create_line(x, 150, 150, x+150, fill=color1)
        canvas.create_line(0, x+150, x, 300, fill=color2)

#q4
for x in range(0, 150, 10):
        canvas.create_line(x+150, 150, 300, x+150, fill=color1)
        canvas.create_line(150, x+150, x+150, 300, fill=color2)

line_in_the_middle()
# draw_nice_pic(20, 0, 150, 'purple', 'green')
# draw_nice_pic(20, 150, 300, 'purple', 'green')
# draw_nice_pic(20, 150, 150, 'purple', 'green')
# draw_nice_pic(20, 300, 300, 'purple', 'green')


root.mainloop()
