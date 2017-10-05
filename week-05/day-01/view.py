from tkinter import *
from PIL import Image, ImageTk
from map import Map
from entity import *



class DrawMap():
    def __init__(self):    
        self.size = 720
        self.root = Tk()
        self.map = Map()
        self.root.configure(background ='black')
        self.canvas = Canvas(self.root, width=self.size, height=self.size,bg="white",bd=0)
        self.canvas.focus_set()
        self.canvas.pack()
        self.image1 = PhotoImage(file = 'floor.png')
        self.image2 = PhotoImage(file = 'wall.Png')
        self.hero_down = PhotoImage(file = 'hero-down.Png')
        self.hero_right = PhotoImage(file = 'hero-right.Png')
        self.hero_left = PhotoImage(file = 'hero-left.Png')
        self.hero_up = PhotoImage(file = 'hero-up.Png')
    

    def drawing_map(self):
        for y in range(len(self.map.map)):
            for x in range(len(self.map.map)):
                if self.map.map[y][x] == 0:
                    self.canvas.create_image(x*72, y*72, anchor = NW, image = self.image1)
                elif self.map.map[y][x] == 1:
                    self.canvas.create_image(x*72, y*72, anchor = NW, image = self.image2)

    def drawing_hero(self, x, y):
        self.hero_img = self.canvas.create_image(x, y, anchor = NW, image = self.hero_down)

    def update_costume(self, costume):
        self.costume = costume
        self.canvas.itemconfigure(self.hero_img, image=self.costume)
    
    def move_entity(self, x, y):
        print(y)
        self.canvas.move(self.hero_img, x, y)

    def show(self):
        self.root.mainloop()