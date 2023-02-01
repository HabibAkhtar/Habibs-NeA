import pygame
from pygame.locals import *
from .loadImages import *
from .computerRepresentation import *

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
        #Making sure an error doesnt pop up if any part of the piece is off the screen(allows human error)
        movement[0]=0
    
            
def draggingPiece(piece_rectX,piece_rectY):
    newX,newY=pygame.mouse.get_pos()
    piece_rectX=piece_rectX
    piece_rectY=piece_rectY
    #Reassigning the rects of the image given so that no matter what piece is clicked on it moves 
    if movement[0]==1:
        piece_rectX,piece_rectY= newX,newY
        
            #Moves the piece to the square the mouse is in is the square is let go



def queenValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    if piece_rect in allQueens:
        if (pieceRow-ogPieceRow) == (pieceCol- ogPieceCol) or (pieceRow-ogPieceRow)==(ogPieceCol-pieceCol) or pieceRow== ogPieceRow or pieceCol== ogPieceCol:
            validCol=True
            validRow=True
        return validCol,validRow


        
def rookValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    if piece_rect in allRooks:
        if pieceRow == ogPieceRow or pieceCol== ogPieceCol:
        #The rook can move anywhere along the row its on , or anywhere along the column its on 
            validCol=True
            validRow=True
        return validCol,validRow




def bishopValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    if piece_rect in allBishops:
        if (pieceRow-ogPieceRow) == (pieceCol-ogPieceCol) or (pieceRow-ogPieceRow)==(ogPieceCol-pieceCol):
            validCol=True
            validRow=True
        return validCol,validRow


def pawnValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect,piecerepresentation):
    validCol=False
    validRow=False
    validMove=False
    if piece_rect in allPawns:
        if 'b' in piecerepresentation:
        #Condition above is checking if the piece is black
            if ogPieceRow==1 :
                if ((pieceRow-ogPieceRow)==2 and pieceCol==ogPieceCol) or ((pieceRow-ogPieceRow)==1 and pieceCol==ogPieceCol) and (chessBoard[pieceRow][pieceCol]==' '):
                        validMove=True
                elif chessBoard[ogPieceRow+1][ogPieceCol-1]!=' ' or chessBoard[ogPieceRow+1][ogPieceCol+1]!=' ':
                    if (pieceRow-ogPieceRow)==1 and ((pieceCol-ogPieceCol)==1 or (pieceCol-ogPieceCol)==-1):
                            if 'b' not in chessBoard[pieceRow][pieceCol]:
                                validMove=True
            elif ogPieceRow!=1:
                if ((pieceRow-ogPieceRow)==1) and (pieceCol==ogPieceCol) and chessBoard[pieceRow][pieceCol]==' ' :
                        validMove=True
            if ogPieceCol==7:
                if chessBoard[ogPieceRow+1][ogPieceCol-1]!=' ':
                    if (pieceRow-ogPieceRow)==1 and ((pieceCol-ogPieceCol)==1 or (pieceCol-ogPieceCol)==-1):
                        if 'b' not in chessBoard[pieceRow][pieceCol]:
                            validMove=True
            else:
                if chessBoard[ogPieceRow+1][ogPieceCol-1]!=' ' or chessBoard[ogPieceRow+1][ogPieceCol+1]!=' ':
                    if (pieceRow-ogPieceRow)==1 and ((pieceCol-ogPieceCol)==1 or (pieceCol-ogPieceCol)==-1):
                        if 'b' not in chessBoard[pieceRow][pieceCol]:
                            validMove=True
            if validMove:
                validCol=True
                validRow=True
        elif 'w' in piecerepresentation:
            if ogPieceRow==6:
                if ((pieceRow-ogPieceRow)==-2 and pieceCol==ogPieceCol) or ((pieceRow-ogPieceRow)==-1 and pieceCol==ogPieceCol) and (chessBoard[pieceRow][pieceCol]==' '):
                    validMove=True
                elif chessBoard[ogPieceRow-1][ogPieceCol-1]!=' ' or chessBoard[ogPieceRow-1][ogPieceCol+1]!=' ':
                    if (pieceRow-ogPieceRow)==-1 and ((pieceCol-ogPieceCol)==1 or (pieceCol-ogPieceCol)==-1):
                        if 'w' not in chessBoard[pieceRow][pieceCol]:
                            validMove=True
            elif ogPieceRow!=6:
                if(pieceRow-ogPieceRow)==-1 and pieceCol==ogPieceCol and (chessBoard[pieceRow][pieceCol]==' '):
                    validMove=True
            if ogPieceCol==7:
                if chessBoard[ogPieceRow-1][ogPieceCol-1]!=' ':
                        if (pieceRow-ogPieceRow)==-1 and ((pieceCol-ogPieceCol)==1 or (pieceCol-ogPieceCol)==-1):
                            if 'w' not in chessBoard[pieceRow][pieceCol]:
                                validMove=True
            else:
                if chessBoard[ogPieceRow-1][ogPieceCol-1]!=' ' or chessBoard[ogPieceRow-1][ogPieceCol+1]!=' ':
                    if (pieceRow-ogPieceRow)==-1 and ((pieceCol-ogPieceCol)==1 or (pieceCol-ogPieceCol)==-1):
                        if 'w' not in chessBoard[pieceRow][pieceCol]:
                            validMove=True
            
            if validMove:
                validCol=True
                validRow=True
        return validCol,validRow


def knightValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    validMove=False
    #All the possible conditions for the knight to move set validMove to true
    #This code cant be grouped together e.g( pieceRow-ogPieceRow)==1 OR -1 as then it will create an infinite possible number of combinations and let the piece move without limitations
    if (pieceRow-ogPieceRow)== 2 and (pieceCol-ogPieceCol)==1 :
        validMove=True
    if (pieceRow-ogPieceRow)==-2 and (pieceCol-ogPieceCol)==-1:
        validMove=True
    if (pieceRow-ogPieceRow)==-2 and (pieceCol-ogPieceCol)==1:
        validMove=True
    if (pieceRow-ogPieceRow)== 2 and (pieceCol-ogPieceCol)==-1:
        validMove=True
    if (pieceRow-ogPieceRow)==1  and (pieceCol- ogPieceCol)==2:
        validMove=True
    if (pieceRow-ogPieceRow)==-1  and (pieceCol- ogPieceCol)==-2:
        validMove=True
    if (pieceRow-ogPieceRow)==-1  and (pieceCol- ogPieceCol)==2:
        validMove=True
    if (pieceRow-ogPieceRow)==1  and (pieceCol- ogPieceCol)==-2:
        validMove=True

    if piece_rect in allKnights:
        if validMove:
            validCol=True
            validRow=True
        return validCol,validRow


def kingValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    validMove=False
    if piece_rect in allKings:
        if (pieceRow-ogPieceRow)==1  and (pieceCol==ogPieceCol):
            validMove=True
        elif (pieceRow-ogPieceRow)==-1  and (pieceCol==ogPieceCol):
            validMove=True
        elif (pieceRow==ogPieceRow) and (pieceCol-ogPieceCol)==1:
            validMove=True
        elif (pieceRow==ogPieceRow) and (pieceCol-ogPieceCol)==-1:
            validMove=True
        elif (pieceRow-ogPieceRow)==1 and (pieceCol-ogPieceCol)==1:
            validMove=True
        elif (pieceRow-ogPieceRow)==-1 and (pieceCol-ogPieceCol)==-1:
            validMove=True
        elif (pieceRow-ogPieceRow)==-1 and (pieceCol-ogPieceCol)==1:
            validMove=True
        elif (pieceRow-ogPieceRow)==1 and (pieceCol-ogPieceCol)==-1:
            validMove=True
        if validMove:
            validCol=True
            validRow=True
        return validCol,validRow

def moveValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect,piecerepresentation):
    #This sub routine checks what piece is trying to be moved and calls the correct sub routine based on the piece 
    for i,rect in enumerate(rectsToBlit):
        if rect == piece_rect:
            if rect in allRooks:
                validCol,validRow=rookValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
                return validCol,validRow
            if rect in allQueens:
                validCol,validRow=queenValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
                return validCol,validRow
            if rect in allBishops:
                validCol,validRow=bishopValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
                return validCol,validRow
            if rect in allPawns:
                validCol,validRow=pawnValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect,piecerepresentation)
                return validCol,validRow
            if rect in allKnights:
                validCol,validRow=knightValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
                return validCol,validRow
            if rect in allKings:
                validCol,validRow=kingValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
                return validCol,validRow

