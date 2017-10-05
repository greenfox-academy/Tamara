from tkinter import *
from PIL import Image, ImageTk
from map import Map
from entity import *
from view import DrawMap

class Game(object):
    def __init__(self):
        self.view = DrawMap()
        self.view.drawing_map()
        self.hero = Hero(0, 0)
        self.view.drawing_hero(self.hero.x, self.hero.y)
        self.view.root.bind("<KeyPress>", self.moving)
        self.view.show()

    def moving(self, e):
        print(self.hero.x, self.hero.y)
        if (e.keysym == 'Up'):
            self.hero.move_entities(self.hero.x, self.hero.y-1)    
            self.view.move_entity(0, -72)
            self.view.update_costume(self.view.hero_up)
        elif (e.keysym == 'Down'):
            self.hero.move_entities(self.hero.x, self.hero.y+1)          
            self.view.move_entity(0, 72)
            self.view.update_costume(self.view.hero_down)            
        elif (e.keysym == 'Right'):
            self.hero.move_entities(self.hero.y+1, self.hero.x)    
            self.view.move_entity(72,0)            
            self.view.update_costume(self.view.hero_right)            
        elif (e.keysym == 'Left'):          
            self.hero.move_entities(self.hero.y-1, self.hero.x)    
            self.view.move_entity(-72,0)
            self.view.update_costume(self.view.hero_left)                

game = Game()