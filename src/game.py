import pygame
import random
from pygame import *
from Player import Player
from Food import Food

pygame.init()

width=600
heigth=600
window=pygame.display.set_mode((width,heigth))
clock=pygame.time.Clock()

score=0
font = pygame.font.SysFont("comicsans",30,True)

green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
Lblue=(0, 255, 255)

colors=[green,blue,red,Lblue]

pacman=Player(width//2,heigth//2,10,2,width,heigth)
foods=[]

run=True
while run:
    clock.tick(120)
    pacman.move()
    pacman.show(window)

    if len(foods)==0:
        foods.append(Food(random.randint(0,width),
                            random.randint(0,heigth),
                            10,
                            random.choice(colors)
                            )
                        )

    for food in foods:
        food.show(window)
        if pygame.Rect.colliderect(pacman.hitbox,food.hitbox):
            if food.color==red:
                score+=10
            elif food.color==green:
                score+=15
            elif food.color==Lblue:
                score+=20
            elif food.color==blue:
                score+=30
            
            foods.remove(food)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    text=font.render("Score: "+ str(score),1,(255,255,255))
    window.blit(text,(width-150,30))

    pygame.display.update()
    window.fill((0,0,0))

pygame.quit()