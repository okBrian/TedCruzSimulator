import pygame
import GameObject 
class Player(GameObject.GameObject):
    def __init__(self, image, pos): 
        up = False
        GameObject.GameObject.__init__(self, image, pos)
    def jump(self, screen):
        print("The Player has jumped")
        if self.pos[1] > 100 and not self.up:
            self.pos[1]-=5
            up = True
        if self.pos[1] == 100:
            up = False
            self.pos[1]-=1
        if self.pos[1] <= 100:
            self.pos[1]+=5