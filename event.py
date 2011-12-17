#! /usr/bin/env python
############################################################################
# File name :event.py
# Purpose :  A Small Demo Practice Prgram using Pygame API
# Usages : Tells About The Events And Related Parameters. Useful For Event Handling
# Start date : 17/12/2011
# End date : 17/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Dependency:  None 
############################################################################

#import modules
import pygame
from pygame.locals import *
from sys import exit


#initalizing variables (setting up the stage)
pygame.init()
a=pygame.display.set_mode((650,400),RESIZABLE,32)
pygame.display.set_caption("Event list ")
font=pygame.font.SysFont("arial",16)
back=pygame.Surface(a.get_size()) 
back=back.convert()
back.fill((255,255,255))


#main loop which displays the events related information 
while True:
 for i in pygame.event.get():
  if i.type==QUIT:
   exit()
  else:
   text=font.render("%s"%i,1,(10,10,10),(255,255,255))
  a.blit(back,(0,0))
  a.blit(text,(0,0))
  pygame.display.update()


