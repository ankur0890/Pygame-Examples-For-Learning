#! /usr/bin/env python
############################################################################
# File name :soundPlay.py
# Purpose : Demostrating Audio File Involvement In A Pygame Program 
# Start date : 30/12/2011
# End date : 30/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Reference : Game Programming By Andy Harris
# Dependancy : yikes.ogg 
############################################################################

import pygame
from pygame.locals import *


pygame.init()
pygame.mixer.init() #mixer module Intialization

def main():
  screen=pygame.display.set_mode((640,480),0,24)
  pygame.display.set_caption('Sound Testing')
  sound=pygame.mixer.Sound('yikes.wav') #creating an audio object
  font=pygame.font.SysFont('arial',30)
  soundFont=font.render("Press Space To Hear A Sound",True,(0,255,0)) 
  while 1:
      pressed=pygame.key.get_pressed()
      for i in pygame.event.get():
          if i.type==QUIT or pressed[K_q]:
              exit()
          elif pressed[K_SPACE]:
              sound.play()  #time to play
      screen.blit(soundFont,(100,100))
      pygame.display.flip()


if __name__=='__main__':
    main()
