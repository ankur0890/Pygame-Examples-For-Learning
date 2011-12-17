#! /usr/bin/env python
############################################################################
# File name : rotation.py
# Purpose : A Small Demo Practice Prgram using Pygame API
# Usages : Simplest rotation program using transform class
# Start date : 17/12/2011
# End date : 17/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Dependency : naughty.png 
############################################################################

import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen=pygame.display.set_mode((640,480),0,0)
pygame.display.set_caption("Rotation using transform module")

image=pygame.image.load("naughty.png").convert_alpha()
image2=image
a=0
clock=pygame.time.Clock()
while True:
 for i in pygame.event.get():
  if i.type==QUIT:
   exit()
 screen.fill((0,0,0))
 rotation=pygame.mouse.get_rel()
 buttonpress=pygame.mouse.get_pressed()
 press=pygame.key.get_pressed()
 screen.blit(image2,(100-(image2.get_width()/2),100-(image2.get_height()/2)))
 if rotation[0] and buttonpress[0]:
  a=a+rotation[0]
  image2=pygame.transform.rotate(image,a)
 if press[K_LEFT]:
  a=a+10
  image2=pygame.transform.rotate(image,a)
 if press[K_RIGHT]:
  a=a-10
  image2=pygame.transform.rotate(image,a)
 pygame.display.update() 
 clock.tick(15)


