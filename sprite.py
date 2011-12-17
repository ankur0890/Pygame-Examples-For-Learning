#! /usr/bin/env python
############################################################################
# File name : sprite.py
# Purpose :   A Small Demo Practice Prgram using Pygame API
# Usages : Teaches Us How To Use Sprites
# Start date : 17/12/2011
# End date : 17/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Dependency : fireSprite.png 
############################################################################

import pygame
from pygame.locals import *
from sys import exit

counter=0
def Update():
 global counter
 counter=(counter+1)%7

def sprite(w, h):
    a=[]
    clock=pygame.time.Clock()
    screen=pygame.display.set_mode((200,200),0,24)
    image = pygame.image.load("fireSprite.png").convert_alpha()
    width,height=image.get_size()
    for i in xrange(int(width/w)):
        a.append(image.subsurface((i*w,0,w,h)))
    while True:
     for i in pygame.event.get():
      if i.type==QUIT:
       exit()
     screen.fill((0,0,0)) 
     screen.blit(a[counter],(100,100))
     Update()
     pygame.display.update()
     clock.tick(5)

sprite(20,20)


