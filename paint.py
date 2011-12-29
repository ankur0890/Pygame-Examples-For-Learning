#! /usr/bin/env python
############################################################################
# File name :paint.py
# Purpose : Demo of Painting Program Made using Pygame API
# Usages : You can paint through this. Features like save,load,line width can slo be included
# Start date : 26/12/2011
# End date : 28/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Reference : Game Programming By Andy Harris
# How To Run : paint.py
############################################################################

#import all necessary modules
import pygame
from pygame.locals import *


#initializations
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('Let\'s Paint')
background=pygame.Surface(screen.get_size())
background=background.convert()
color=(0,0,0)
startPos=(0,0)
clock=pygame.time.Clock()
background.fill((255,255,255))
font=pygame.font.SysFont('arial',20)
colorName="Black"
welcomeFont=pygame.font.SysFont('arial',30)
colorConfigFont=pygame.font.SysFont('arial',20)
welcomeScreen=True

#mainloop
while 1:
    #welcomescreen
    while welcomeScreen:
       for i in pygame.event.get():
           mainScreenPressed=pygame.key.get_pressed()
           if i.type==QUIT or mainScreenPressed[K_q]:
               exit()
           screen.fill((0,0,0))
           screen.blit(welcomeFont.render("Paint Program Example For Learning",True,(0,255,0)),(100,100))
           screen.blit(colorConfigFont.render("Painting Options",True,(0,255,0)),(100,150))
           screen.blit(colorConfigFont.render("d-Default Color(Black)",True,(0,255,0)),(100,175))
           screen.blit(colorConfigFont.render("b-Blue Color",True,(0,255,0)),(100,200))
           screen.blit(colorConfigFont.render("r-Red Color",True,(0,255,0)),(100,225))
           screen.blit(colorConfigFont.render("y-Yellow Color",True,(0,255,0)),(100,250))
           screen.blit(colorConfigFont.render("g-Green Color",True,(0,255,0)),(100,275))
           screen.blit(colorConfigFont.render("e-Eraser",True,(0,255,0)),(100,300))
           screen.blit(colorConfigFont.render("s-Save Image",True,(0,255,0)),(100,325))
           screen.blit(colorConfigFont.render("l-Load Image",True,(0,255,0)),(100,350))
           screen.blit(welcomeFont.render("Press p for painting",True,(0,255,0)),(100,400))
           pygame.display.flip()
           if mainScreenPressed[K_p]:
               welcomeScreen=False

    #paint screen        
    pressed=pygame.key.get_pressed()
    if pressed[K_r]:
        color=(255,0,0)
        colorName="Red"
    elif pressed[K_g]:
        color=(0,255,0)
        colorName="Green"
    elif pressed[K_b]:
        color=(0,0,255)
        colorName="Blue"
    elif pressed[K_y]:
        color=(255,255,0)
        colorName="Yellow"
    elif pressed[K_e]:
        color=(255,255,255)
        colorNAme="White"
    elif pressed[K_d]:
        color=(0,0,0)
        colorName="Black"
    elif pressed[K_c]:
        color=(0,0,0)
        colorName="Black"
        welcomeScreen=True
    elif pressed[K_s]:
        pygame.image.save(background,'image.png')
    elif pressed[K_l]:
        background=pygame.image.load('image.png')
        colorName="Black"
        color=(0,0,0)


    for i in pygame.event.get():
        if i.type==QUIT or pressed[K_q]:
            exit()
        elif i.type==pygame.MOUSEMOTION:
            endPos=pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()==(1,0,0):
                pygame.draw.line(background,color,startPos,endPos,3)
            startPos=endPos

    screen.blit(background,(0,0))
    if color==(255,255,255):
     screen.blit(font.render("Eraser In Use",True,(0,0,0)),(400,400))
     screen.blit(font.render("Press c for painting options",True,(0,0,0)),(100,400))
    else:
     screen.blit(font.render("Press c for painting options",True,(0,0,0)),(100,400))   
     screen.blit(font.render("Color In Use : %s"%colorName,True,color),(400,400))
    pygame.display.flip()

