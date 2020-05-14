import pygame
from pygame import *

class Food():
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.hitbox=pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)

    def show(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)
        self.hitbox=pygame.Rect(self.x-self.radius,self.y-self.radius,self.radius*2,self.radius*2)
        #pygame.draw.rect(surface,(255,255,255),self.hitbox,1)

