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
        sound = pygame.mixer.Sound("./Pieces/pieceDown.wav")
        sound.set_volume(0.2)
        sound.play()
        ogPieceCol=startX//squareSize
        ogPieceRow=startY//squareSize
        newX,newY=pygame.mouse.get_pos()
        pieceCol=newX//squareSize
        pieceRow=newY//squareSize
        pieceRow=int(pieceRow)
        pieceCol=int(pieceCol)
        validCol,validRow=moveValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)

        #If the row and col is classed as valid using the 2 subroutines which have been called above , then the piece will be moved 
        if validRow and validCol:
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
                            piecesToBlit.pop(i)
                            rectsToBlit.pop(i)
                            compRepOfPieces.pop(i)
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





def whichPiece(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    if piece_rect==queenB_rect or queenW_rect:
        validCol,validRow=queenVal(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
    
    if piece_rect==rookB1_rect or rookB2_rect or rookW1_rect or rookW2_rect:
        validCol,validRow=rookVal(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
    return validCol,validRow


def queenVal(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    if piece_rect==queenB_rect or piece_rect==queenW_rect:
        if (pieceRow-ogPieceRow) == (pieceCol- ogPieceCol) or (pieceRow-ogPieceRow)==(ogPieceCol-pieceCol) or pieceRow== ogPieceRow or pieceCol== ogPieceCol:
            validCol=True
            validRow=True
        return validCol,validRow
    else:
        return validCol,validRow

def rookVal(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    if piece_rect== rookB1_rect or piece_rect==rookB2_rect or piece_rect==rookW1_rect or piece_rect==rookW2_rect:
        if pieceRow == ogPieceRow or pieceCol== ogPieceCol:
        #The rook can move anywhere along the row its on , or anywhere along the column its on 
            validCol=True
            validRow=True
        return validCol,validRow
    else:
        return validCol,validRow




moveValidationList=[queenVal]


def moveValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    for i,rect in enumerate(rectsToBlit):
        if rect == piece_rect:
            if rect in allRooks:
                validCol,validRow=rookVal(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
                return validCol,validRow
            if rect in allQueens:
                validCol,validRow=queenVal(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect)
                return validCol,validRow



#The colValidation and rowValidation subroutines need to be 2 seperate subroutines because there will be specific circumstances 
'''
def colValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):

    elif piece_rect==bishopB1_rect or piece_rect==bishopB2_rect or piece_rect==bishopW1_rect or piece_rect==bishopW2_rect:
        if (pieceRow-ogPieceRow) == (pieceCol- ogPieceCol) or (pieceRow-ogPieceRow)==(ogPieceCol-pieceCol):
        #This makes sure all the bishops can go as many spaces as possible diagonally 
            validCol=True
            return validCol






def rowValidation(pieceRow,ogPieceRow,pieceCol,ogPieceCol,piece_rect):
    validRow=False

    if piece_rect==queenB_rect or piece_rect==queenW_rect:
        if (pieceRow-ogPieceRow) == (pieceCol- ogPieceCol) or (pieceRow-ogPieceRow)==(ogPieceCol-pieceCol) or pieceRow== ogPieceRow or pieceCol== ogPieceCol:
            validRow=True

        return validRow
    
    elif piece_rect== rookB1_rect or piece_rect==rookB2_rect or piece_rect==rookW1_rect or piece_rect==rookW2_rect:
        if pieceRow== ogPieceRow or pieceCol== ogPieceCol:
            validRow=True
        return validRow

    elif piece_rect==bishopB1_rect or piece_rect==bishopB2_rect or piece_rect==bishopW1_rect or piece_rect==bishopW2_rect:
        if (pieceRow-ogPieceRow) == (pieceCol-ogPieceCol) or (pieceRow-ogPieceRow)==(ogPieceCol-pieceCol):
            validRow=True
        return validRow
            
'''
                    

''' 
The issue with the code above is that if the queen is in the starting pos of the rook , It cant go diagonally and if the queen is in the starting pos of the bishop ,
it can only go diagonally 
'''

#Make an array with every function of the moveValidations e.g [rookVal,queenVal]
#use a base validation function (like the rowVal function in speech marks above )
#loop through the pieces to blit 