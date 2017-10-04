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
                

class Entity(object):
    def __init__(self):
        self.hero = PhotoImage(file = 'hero-down.Png')
        self.hero_right = PhotoImage(file = 'hero-right.Png')
        self.hero_left = PhotoImage(file = 'hero-left.Png')
        self.hero_up = PhotoImage(file = 'hero-up.Png')        
        self.drawing_entity()

    def drawing_entity(self):
        self.hero_img = canvas.create_image(0, 0, anchor = NW, image = self.hero)

    def move(self, dx, dy):
        canvas.move(hero.hero_img, dx, dy )

    def update_costume(self, costume):
        self.costume = costume
        canvas.itemconfigure(self.hero_img, image=self.costume)
    
    def moving(self, e):
        if (e.keysym == 'Up'):
            self.move(0,-72)
            self.update_costume(self.hero_up)
        elif (e.keysym == 'Down'):
            self.move(0,72)
            self.update_costume(self.hero)            
        elif (e.keysym == 'Right'):
            self.move(72,0)            
            self.update_costume(self.hero_right)            
        elif (e.keysym == 'Left'):
            self.move(-72,0)
            self.update_costume(self.hero_left)                


canvas.pack()
map_draw = DrawMap()
hero = Entity()
root.bind("<KeyPress>", hero.moving)
canvas.focus_set()

root.mainloop()