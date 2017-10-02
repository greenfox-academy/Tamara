from tkinter import *
from PIL import Image, ImageTk
from map import Map
from entity import *

size = 720
root = Tk()
map = Map()
root.configure(background ='black')
canvas = Canvas(root, width=size, height=size,bg="white",bd=0)
canvas.pack()
class DrawMap():
    def __init__(self):    
        self.image1 = PhotoImage(file = 'floor.png')
        self.image2 = PhotoImage(file = 'wall.Png')
        self.drawing_map()

    def drawing_map(self):
        for y in range(len(map.map)):
            for x in range(len(map.map)):
                if map.map[y][x] == 0:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.image1)
                elif map.map[y][x] == 1:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.image2)
                

class DrawEntity:
    def __init__(self):
        self.hero = PhotoImage(file = 'hero-down.Png')
        self.drawing_entity()

    def drawing_entity(self):
        self.entity_img = canvas.create_image(0, 0, anchor = NW, image = self.hero)

class Entity(object):
    def __init__(self):
        pass

    def move(self, dx, dy):
        canvas.move(hero.entity_img, dx, dy )

entities = Entity()
def moving(e):
    if (e.keysym == 'Up'):
        entities.move(0,-72)
    elif (e.keysym == 'Down'):
        entities.move(0,72)
    elif (e.keysym == 'Right'):
        entities.move(72,0)            
    elif (e.keysym == 'Left'):
        entities.move(-72,0)

canvas.pack()
map_draw = DrawMap()
hero = DrawEntity()
root.bind("<KeyPress>", moving)
canvas.focus_set()

root.mainloop()