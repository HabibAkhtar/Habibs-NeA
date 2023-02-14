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
        if not validRow or not validCol:
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
            pieceCounter=0
            holder=' '
            if chessBoard[pieceRow][pieceCol] != ' ' and chessBoard[pieceRow][pieceCol] != piecerepresentation:
            #These conditions above are checking if there is a piece where the moving piece is trying to move to
                for i,piece in enumerate(compRepOfPieces):
            #These lines of code is repsonsible for killing the pieces if the pieces are taken 
                    if piece == chessBoard[pieceRow][pieceCol]:
                        piecesToBlit.pop(i)
                        rectsToBlit.pop(i)
                        compRepOfPieces.pop(i)

            for i,sublist in enumerate(chessBoard):
            #The enumerate function adds an index value for every item in the list
                if piecerepresentation in sublist:
                    chessBoard[i][sublist.index(piecerepresentation)]=' '

                chessBoard[pieceRow][pieceCol]=piecerepresentation
                for x in sublist:
                    # without the 2 if statements below , if a piece is moved left in the same row , the computer will register the piece twice 
                    if x == piecerepresentation:
                        chessBoard[i][sublist.index(piecerepresentation)]=holder
                        pieceCounter+=1
                    if pieceCounter > 1:
                        holder = ' '


            if pieceRow>7 or pieceCol>7:
                pieceCol-=1
                pieceRow-=1
                if chessBoard[pieceRow][pieceCol] != ' ' and chessBoard[pieceRow][pieceCol] != piecerepresentation:
                #These conditions above are checking if there is a piece where the moving piece is trying to move to
                    for i,piece in enumerate(compRepOfPieces):
                        if piece == chessBoard[pieceRow][pieceCol]:
                #These lines of code is repsonsible for killing the pieces if the pieces are taken 
                            piecesToBlit.remove(i)
                            rectsToBlit.remove(i)
                            compRepOfPieces.remove(i)
                chessBoard[pieceRow][pieceCol]=piecerepresentation
            
                for i,sublist in enumerate(chessBoard):
            #The enumerate function adds an index value for every item in the list
                    if piecerepresentation in sublist:
                        chessBoard[i][sublist.index(piecerepresentation)]=' '

                    chessBoard[pieceRow][pieceCol]=piecerepresentation
                    for x in sublist:
                        # without the 2 if statements below , if a piece is moved left in the same row , the computer will register the piece twice 
                        if x == piecerepresentation:
                            chessBoard[i][sublist.index(piecerepresentation)]=holder
                            pieceCounter+=1
                        if pieceCounter > 1:
                            holder = ' '

        #Making sure an error doesnt pop up if any part of the piece is off the screen(allows human error)
        movement[0]=0
    
            
        
        
        
            



