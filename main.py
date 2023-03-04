import pygame, sys
from chess.chessboard import *
from chess.computerRepresentation import *
from chess.loadImages import *
from chess.handlingEvents import *
#BUGS IN THE CODE 

#code check and checkmate

#Code in turns 
#THEN UR DONE AND CAN MOVE ONTO ADDITIONAL OBJECTIVES
#undo/redo function
#Add a timer
#saving a game with a file 

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
            #for row in chessBoard:
            #   print(row)
            




   

    for i,j in enumerate(piecesToBlit):
        WINDOW.blit(j,rectsToBlit[i])
    pygame.display.flip()
    pygame.display.update()
 


