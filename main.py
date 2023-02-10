import pygame, sys
from chess.chessboard import *
from chess.computerRepresentation import *
from chess.loadImages import *
from chess.handlingEvents import *


pygame.init()
pygame.mixer.init()
Running=True
while Running:
    #calls the class that creates the chessboard 
    createChessboard(WIDTH, HEIGHT, WINDOW)
    for i,j in enumerate(piecesToBlit):
        WINDOW.blit(j,rectsToBlit[i])
    #Blits all pieces onto the screen

    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            Running=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            currentX,currentY=pygame.mouse.get_pos()
            for i,j in enumerate(rectsToBlit):
                if j.collidepoint(currentX,currentY):
                    piece_rect=j
                    pieceRep=compRepOfPieces[i]
                    
            startX,startY=clickPiece(piece_rect)
            

        elif event.type == pygame.MOUSEBUTTONUP:
            dropPiece(pieceRep,piece_rect,startX,startY)
            for row in chessBoard:
                print(row)

        #elif event.type == pygame.MOUSEMOTION:
            #The parameters given could be any of the rects of the pieces as it gets reassigned in the method 
        #    draggingPiece(rookB1_rect.centerx,rookB1_rect.centery)
   

    for i,j in enumerate(piecesToBlit):
        WINDOW.blit(j,rectsToBlit[i])
    pygame.display.flip()
    pygame.display.update()
 


