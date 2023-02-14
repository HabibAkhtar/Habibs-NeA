from .loadImages import *
from .computerRepresentation import *

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
    validMove=True
    if piece_rect in allRooks:
        if pieceRow == ogPieceRow or pieceCol== ogPieceCol:
        #The rook can move anywhere along the row its on , or anywhere along the column its on
        #The conditions below make sure the rook cant jump over other pieces 
            if pieceRow!= ogPieceRow:
                #Piece is moving up or down 
                if pieceRow>ogPieceRow:
                    #Piece is moving down
                    #This makes sure that the piece cant jump over any pieces below it 
                    for i in range (pieceRow-1,ogPieceRow,-1):
                        #Checks if there is any pieces in between where the piece was and where it is trying to move ,
                        #If there is then the move is illegal 
                        if chessBoard[i][pieceCol] != ' ':
                            validMove= False
                elif ogPieceRow>pieceRow:
                    #Piece is moving up
                    #This makes sure that the piece cant jump over any pieces above it 
                    for x in range (pieceRow+1,ogPieceRow):
                        #Checks if there is any pieces in between where the piece was and where it is trying to move ,
                        #If there is then the move is illegal 
                        if chessBoard[x][pieceCol]!= ' ':
                            validMove=False
            elif pieceCol != ogPieceCol:
                #Piece is moving sideways 
                if pieceCol>ogPieceCol:
                    #Piece is moving right
                    #This code makes sure that the piece cant jump over any pieces to the right of it 
                    for y in range (pieceCol-1,ogPieceCol,-1):
                        #Checks if there is any pieces in between where the piece was and where it is trying to move ,
                        #If there is then the move is illegal 
                        if chessBoard[pieceRow][y] !=' ':
                            validMove=False
                elif ogPieceCol>pieceCol:
                    #Piece is moving left 
                    #This code makes sure that the piece cant jump over any pieces to the left of it 
                    for z in range (pieceCol+1,ogPieceCol):
                        #Checks if there is any pieces in between where the piece was and where it is trying to move ,
                        #If there is then the move is illegal 
                        if chessBoard[pieceRow][z] != ' ':
                            validMove=False


            
            if validMove and chessBoard[pieceRow][pieceCol][0]!=chessBoard[ogPieceRow][ogPieceCol][0]:
                #This condition checks if the move has been deemed valid and the piece is not taking a piece of its own colour
                validCol=True
                validRow=True
        return validCol,validRow




def bishopValidation(pieceCol,ogPieceCol,pieceRow,ogPieceRow,piece_rect):
    validCol=False
    validRow=False
    validMove=True
    if piece_rect in allBishops:
        if (pieceRow-ogPieceRow) == (pieceCol-ogPieceCol) or (pieceRow-ogPieceRow)==(ogPieceCol-pieceCol):
            if pieceRow>ogPieceRow and pieceCol>ogPieceCol:
                #Piece is moving down and to the right
                for d in range (pieceRow-1,ogPieceRow,-1):
                    for f in range (pieceCol-1,ogPieceCol,-1):
                        if chessBoard[d][f]!=' ':
                            validMove=False
            if validMove:
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
            ogPieceRow=int(ogPieceRow)
            ogPieceCol=int(ogPieceCol)
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
                #If the piece is in row 7 , then it is impossible for a piece to be to the right of it and so checking that position which doesnt exist will cause an error
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
            ogPieceRow=int(ogPieceRow)
            ogPieceCol=int(ogPieceCol)
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
                #If the piece is in row 7 , then it is impossible for a piece to be to the right of it and so checking that position which doesnt exist will cause an error
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
            ogPieceRow=int(ogPieceRow)
            ogPieceCol=int(ogPieceCol)
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
