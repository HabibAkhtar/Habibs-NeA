import pygame
from pygame.locals import *
from .loadImages import *
from .computerRepresentation import *
from .moveRules import *
#Due to a pygame bug this array below is used as a boolean variable , the first index represents a true/false variable 
#If the first index is 1 that represents true whereas if it 0 that represents false
movement=[0]


def clickPiece(piece_rect):
    startX,startY=pygame.mouse.get_pos()
    if piece_rect.collidepoint(startX,startY):
        movement[0]=1
        
        
    return startX,startY
        
def dropPiece(piecerepresentation,piece_rect,startX,startY):
    if movement[0]==1:
        ogPieceCol=startX//squareSize
        ogPieceRow=startY//squareSize
        newX,newY=pygame.mouse.get_pos()
        pieceCol=newX//squareSize
        pieceRow=newY//squareSize
        pieceRow=int(pieceRow)
        pieceCol=int(pieceCol)
        #This subroutine below will see what piece is being selected and then call the correct subroutine
        #This is to check if the move that is trying to be made is valid or not 
        validCol,validRow=moveValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect,piecerepresentation)
        if not validRow or not validCol :
            invalidMoveSound=pygame.mixer.Sound("./Pieces/invalidMove.wav")
            invalidMoveSound.set_volume(0.2)
            invalidMoveSound.play()
        if validRow and validCol:
            sound = pygame.mixer.Sound("./Pieces/pieceDown.wav")
            sound.set_volume(0.2)
            sound.play()
            piece_rect.y=squareSize*pieceRow
            piece_rect.x=squareSize*pieceCol
            #Pinning the piece to a square

            updateCompRep(pieceRow,pieceCol,ogPieceRow,ogPieceCol,piecerepresentation)
        


        movement[0]=0
    
            
        
        
def updateCompRep(pieceRow,pieceCol,ogPieceRow,ogPieceCol,piecerepresentation):
    if chessBoard[pieceRow][pieceCol] != ' ' and chessBoard[pieceRow][pieceCol] != piecerepresentation:
        #These conditions above are checking if there is a piece where the moving piece is trying to move to    
            for i,piece in enumerate(compRepOfPieces):
        #These lines of code is repsonsible for killing the pieces if the pieces are taken
            
                if piece == chessBoard[pieceRow][pieceCol]:
                    piecesToBlit.pop(i)
                    rectsToBlit.pop(i)
                    compRepOfPieces.pop(i)
    chessBoard[ogPieceRow][ogPieceCol]= ' '
    chessBoard[pieceRow][pieceCol]= piecerepresentation    

          
                
#The code below is responsible for turn taking in the game 
        



