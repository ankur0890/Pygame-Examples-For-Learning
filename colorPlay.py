#! /usr/bin/env python
############################################################################
# File name : ../Pygame-Examples-For-Learning/colorPlay.py
# Purpose : A Small Demo Practice Prgram using Pygame API
# Usages : You can play with colors by changing there Intensites 
# Start date : 14/12/2011
# End date : 14/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# How To Run: python colorPlay.py 
############################################################################

#import all the necessary modules
import pygame
from pygame.locals import *


#initializations
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Color Play")
font=pygame.font.SysFont('arial',10)
redFont=font.render('Red',True,(0,0,0))
greenFont=font.render("Green",True,(0,0,0))
blueFont=font.render("Blue",True,(0,0,0))
background=pygame.Surface(screen.get_size())
background=background.convert()
red=1
green=2
blue=3
redX=75
redY=125
greenX=175
greenY=125
blueX=275
blueY=125
clock=pygame.time.Clock()
currentColor=red

#Game Loop
while 1:
    pressed=pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type==QUIT or pressed[K_q]:
            exit()

    
    if pressed[K_DOWN] and currentColor==red:
        redY=redY+1
    elif pressed[K_UP] and currentColor==red:
        redY=redY-1

    if pressed[K_DOWN] and currentColor==green:
        greenY=greenY+1
    elif pressed[K_UP] and currentColor==green:
        greenY=greenY-1

    if pressed[K_DOWN] and currentColor==blue:
        blueY=blueY+1
    elif pressed[K_UP] and currentColor==blue:
        blueY=blueY-1
        


    redIntensity=redY-100
    greenIntensity=greenY-100
    blueIntensity=blueY-100

    if redIntensity<0:
        redIntensity=0
        redY=100
    elif redIntensity>255:
        redIntensity=255
        redY=355
    if greenIntensity<0:
        greenIntensity=0
        greenY=100
    elif greenIntensity>255:
        greenIntensity=255
        greenY=355

    if blueIntensity<0:
        blueIntensity=0
        blueY=100
    elif blueIntensity>255:
        blueIntensity=255
        blueY=356

    background.fill((redIntensity,greenIntensity,blueIntensity))

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    pygame.draw.line(screen,(255,0,0),(100,100),(100,356),1)
    pygame.draw.line(screen,(0,255,0),(200,100),(200,356),1)
    pygame.draw.line(screen,(0,0,255),(300,100),(300,356),1)
    pygame.draw.rect(screen,(255,0,0),((redX,redY),(50,50)),0)
    pygame.draw.rect(screen,(0,255,0),((greenX,greenY),(50,50)),0)
    pygame.draw.rect(screen,(0,0,255),((blueX,blueY),(50,50)),0)
    screen.blit(redFont,(redX+10,redY+10))
    screen.blit(greenFont,(greenX+10,greenY+10))
    screen.blit(blueFont,(blueX+10,blueY+10))
    screen.blit(font.render("%i"%redIntensity,True,(0,0,0)),(redX+10,redY+30))
    screen.blit(font.render("%i"%greenIntensity,True,(0,0,0)),(greenX+10,greenY+30))
    screen.blit(font.render("%i"%blueIntensity,True,(0,0,0)),(blueX+10,blueY+30))
    if pressed[K_RIGHT] or pressed[K_TAB]:
        if currentColor==red:
            currentColor=green
            screen.blit(greenFont,(200,60))
        elif currentColor==green or pressed[K_TAB]:
            currentColor=blue
            screen.blit(blueFont,(300,60))
        elif currentColor==blue or pressed[K_TAB]:
            currentColor=red
            screen.blit(redFont,(100,60))

    if pressed[K_LEFT]:
        if currentColor==red:
            currentColor=blue
            screen.blit(blueFont,(300,60))
        elif currentColor==green:
            currentColor=red
            screen.blit(redFont,(100,60))
        elif currentColor==blue:
            currentColor=green
            screen.blit(greenFont,(200,60))
    clock.tick(15)
    pygame.display.flip()

