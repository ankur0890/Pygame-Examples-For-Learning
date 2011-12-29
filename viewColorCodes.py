#! /usr/bin/env python
############################################################################
# File name : viewColorCodes.py
# Usages :  Will Display All The Color Codes along with the color name and its value
# Start date : 29/12/2011
# End date : 29/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# How To Run : python viewColorCodes.py
# Reference : Game Programming By Andy Harris
############################################################################

import pygame
from pygame.locals import *


#To explore more see the pydoc for pygame.color.THECOLORS
def main():
    for colorName,value in pygame.color.THECOLORS.items():
        print colorName,value


if __name__=="__main__":
    main()

