import pygame
import random
from pygame import *

class Enemy():
    def __init__(self, x, y, width, heigth, vel, s_w, s_h):
        self.x=x
        self.y=y
        self.width=width
        self.heigth=heigth
        self.vel=vel
        self.s_w=s_w
        self.s_h=s_h
        self.hitbox=pygame.Rect(self.x,self.y,self.width,self.heigth)
        self.color=(255,0,255)

        self.tick=0
        self.directions=["up","down","left","right"]
        self.cur_dir=random.choice(self.directions)
        self.new_cur_dir=None

    def show(self,surface):
        pygame.draw.rect(surface,self.color,(self.x,self.y,self.width,self.heigth))
        self.hitbox=pygame.Rect(self.x,self.y,self.width,self.heigth)
        pygame.draw.rect(surface,(255,255,255),self.hitbox,1)

    def move(self):
        self.tick+=1
        if self.tick>=10:
            self.new_cur_dir=random.choice(self.directions)
            if self.cur_dir==self.new_cur_dir:
                self.new_cur_dir=random.choice(self.directions)
            self.tick=0

        if self.new_cur_dir=="up":
            if self.y>0:
                self.y-=self.vel
            else:
                self.x=random.randint(0,self.s_w)
                self.y=random.randint(0,self.s_h)
        
        elif self.new_cur_dir=="down":
            if self.y<self.s_h:
                self.y+=self.vel
            else:
                self.x=random.randint(0,self.s_w)
                self.y=random.randint(0,self.s_h)
        
        elif self.new_cur_dir=="left":
            if self.x<self.s_w:
                self.x+=self.vel
            else:
                self.x=random.randint(0,self.s_w)
                self.y=random.randint(0,self.s_h)
        
        elif self.new_cur_dir=="right":
            if self.x>0:
                self.x-=self.vel
            else:
                self.x=random.randint(0,self.s_w)
                self.y=random.randint(0,self.s_h)
