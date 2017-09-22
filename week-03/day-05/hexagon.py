from tkinter import *
import math
#import time
root = Tk()


canvas = Canvas(root, width='800', height='800')
canvas.pack()

def draw_hexagon(x, y, size):
    # time.sleep(0.01)
    # canvas.update()
    height = math.sqrt(3)/2 * size
    canvas.create_polygon(x, y, x+size/2, y-height, x+size*1.5, y-height, 
                          x+ size*2, y,x+size*1.5, y+ height, x+size/2, y+height, 
                          fill='', outline='black')
    
    
def draw_fractal(x, y, size):
    height = math.sqrt(3)/2 * size
    if size < 70:
        return
    else:
        draw_hexagon(x, y, size)
        draw_fractal(x, y, size/3)
        draw_fractal(x+size/3, y-height/1.5, size/3)    
        draw_fractal(x+size, y-height/1.5, size/3)    
        draw_fractal(x+height*1.54, y, size/3)    
        draw_fractal(x+size, y+height/1.5, size/3)    
        draw_fractal(x+size/3, y+height/1.5, size/3)    
    

draw_fractal(0, 400, 400)

root.mainloop()