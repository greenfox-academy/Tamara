from tkinter import *
from PIL import Image, ImageTk
from map import Map
from entity import *
from view import DrawMap

class Game(object):
    def __init__(self):
        self.view = DrawMap()
        self.view.drawing_map()
        self.view.drawing_hero()
        self.view.root.bind("<KeyPress>", self.moving)
        self.view.show()

    def moving(self, e):
            if (e.keysym == 'Up'):
                self.view.move_entity(0,-72)
                self.view.update_costume(self.view.hero_up)
            elif (e.keysym == 'Down'):              
                self.view.move_entity(0,72)
                self.view.update_costume(self.view.hero)            
            elif (e.keysym == 'Right'):
                self.view.move_entity(72,0)            
                self.view.update_costume(self.view.hero_right)            
            elif (e.keysym == 'Left'):          
                self.view.move_entity(-72,0)
                return self.view.update_costume(self.view.hero_left)                

game = Game()