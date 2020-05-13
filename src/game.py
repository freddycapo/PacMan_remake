import pygame
from pygame import *
from Player import Player

pygame.init()

width=600
heigth=600
window=pygame.display.set_mode((width,heigth))
clock=pygame.time.Clock()

pacman=Player(width//2,heigth//2,10,5,width,heigth)

run=True
while run:
    clock.tick(100)
    pacman.move()
    pacman.show(window)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()
    window.fill((0,0,0))

pygame.quit()