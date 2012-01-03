#! /usr/bin/env python
############################################################################
# File name :boxes.py
# Purpose : Demo Displaying Random Color Squares Usng Sprite Class
# Usages : Learning Purpose
# Start date : 03/01/2012
# End date : 03/01/2012
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Reference : Game Programming By Andy Harris
# How To Run : python boxes.py
############################################################################

#importng necessary modules
import pygame
from pygame.locals import *
from random import randint


pygame.init()
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Boxes All The Way")


#inheritance of Sprite class.every Sprite Must Have image and rect property otherwise it wll give you an exception
class Boxes(pygame.sprite.Sprite):
    def __init__(self,color):   
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.center=(randint(0,640),randint(0,480))


def main():
    background=pygame.Surface(screen.get_size())
    background=background.convert()
    background.fill((0,0,0))
    screen.blit(background,(0,0))
    boxes=[]

    #traversng through every color. see 'pydoc pygame.color.THECOLORS' for more details
    for colorName in pygame.color.THECOLORS:
       boxes.append(Boxes(pygame.color.Color(colorName)))

    allSprites=pygame.sprite.Group(boxes)
 
    while 1:
        for i in pygame.event.get():
          if i.type==QUIT:
                exit()

        #following the CUD Rule (Clear,Update,Draw)
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()


if __name__=='__main__':
    main()

