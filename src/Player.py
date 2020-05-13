import pygame
from pygame import *

class Player():
    def __init__(self,x,y,radius,vel,s_w,s_h):
        self.x=x
        self.y=y
        self.radius=radius
        self.vel=vel
        self.s_w=s_w
        self.s_h=s_h
        self.coulor=(255,128,0)
        self.hitbox=pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
        self.up=False
        self.left=False
        self.right=False
        self.down=False

    
    def show(self,surface):
        pygame.draw.circle(surface,self.coulor,(self.x,self.y),self.radius)
        self.hitbox=pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)

    def move(self):
        keys=pygame.key.get_pressed()
        if keys[K_UP] or keys[K_w]:
            self.up=True
            self.left=False
            self.right=False
            self.down=False
        elif keys[K_DOWN] or keys[K_s]:
            self.down=True
            self.up=False
            self.left=False
            self.right=False
        elif keys[K_RIGHT] or keys[K_d]:
            self.right=True
            self.up=False
            self.left=False
            self.down=False
        elif keys[K_LEFT] or keys[K_a]:
            self.left=True
            self.up=False
            self.right=False
            self.down=False

        if self.up:
            if self.y>0:
                self.y-=self.vel
        elif self.down:
            if self.y<self.s_h:
                self.y+=self.vel
        
        elif self.right:
            if self.x<self.s_w:
                self.x+=self.vel
        elif self.left:
            if self.x>0:
                self.x-=self.vel
        

