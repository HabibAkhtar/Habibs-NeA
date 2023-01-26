import pygame
from pygame.locals import *

pygame.init()


def createChessboard(windowWidth, windowHeight, surface):

    rectWidth = windowWidth/8
    rectHeight = windowHeight/8
    x = 0
    y = 0
    color = None
    colour1=(205,133,63)
    colour2=(245,245,220)

    def createHorizontalRects(x, y, color, color2):
        for i in range(8):

            rects = pygame.Rect(x, y, rectWidth, rectHeight)
            
            if i % 2 == 0:
                pygame.draw.rect(surface, color, rects)
                x += rectWidth
          
            #every even number of tiles the color changes 
            
            else:
                pygame.draw.rect(surface, color2, rects)
                x += rectWidth
            
    x = 0



    for i in range(8):

        if i % 2 == 0:
            createHorizontalRects(x, y, colour1, colour2)
            y += rectHeight

        if i % 2 == 1:
            createHorizontalRects(x, y, colour2,colour1)
            y += rectWidth


