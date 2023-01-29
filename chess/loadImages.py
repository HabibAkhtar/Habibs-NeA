import pygame
from pygame.locals import *


pygame.init()
WIDTH = HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

rookB1=pygame.image.load("./Pieces/black rook.png").convert_alpha()
rookB1=pygame.transform.scale(rookB1,(100,100))
rookB1_rect=rookB1.get_rect()
#Setting the center of the image co ordinates . and the starting co ordinates for the piece
rookB1_rect.centerx=50
rookB1_rect.centery=50



knightB1=pygame.image.load("./Pieces/black knight.png").convert_alpha()
knightB1=pygame.transform.scale(knightB1, (90,90))
knightB1_rect=knightB1.get_rect()
#Setting the center of the image co ordinates . and the starting co ordinates for the piece 
knightB1_rect.centerx=150
knightB1_rect.centery=50


bishopB1=pygame.image.load("./Pieces/black bishop.png").convert_alpha()
bishopB1=pygame.transform.scale(bishopB1,(100,100))
bishopB1_rect=bishopB1.get_rect()
bishopB1_rect.centerx=250
bishopB1_rect.centery=50



queenB=pygame.image.load("./Pieces/black queen.png").convert_alpha()
queenB=pygame.transform.scale(queenB,(100,100))
queenB_rect=queenB.get_rect()
queenB_rect.centerx=350
queenB_rect.centery=50

kingB=pygame.image.load("./Pieces/black king.png").convert_alpha()
kingB=pygame.transform.scale(kingB,(100,100))
kingB_rect=kingB.get_rect()
kingB_rect.centerx=450
kingB_rect.centery=50

bishopB2=pygame.image.load("./Pieces/black bishop.png").convert_alpha()
bishopB2=pygame.transform.scale(bishopB2,(100,100))
bishopB2_rect=bishopB2.get_rect()
bishopB2_rect.centerx=550
bishopB2_rect.centery=50

knightB2=pygame.image.load("./Pieces/black knight.png").convert_alpha()
knightB2=pygame.transform.scale(knightB2,(90,90))
knightB2_rect=knightB2.get_rect()
knightB2_rect.centerx=650
knightB2_rect.centery=50

rookB2=pygame.image.load("./Pieces/black rook.png").convert_alpha()
rookB2=pygame.transform.scale(rookB2,(100,100))
rookB2_rect=rookB2.get_rect()
#Setting the center of the image co ordinates . and the starting co ordinates for the piece
rookB2_rect.centerx=750
rookB2_rect.centery=50


pawnB1=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB1=pygame.transform.scale(pawnB1,(100,100))
pawnB1_rect=pawnB1.get_rect()
pawnB1_rect.centerx=50
pawnB1_rect.centery=150
pawnb1Count=0

pawnB2=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB2=pygame.transform.scale(pawnB2,(100,100))
pawnB2_rect=pawnB2.get_rect()
pawnB2_rect.centerx=150
pawnB2_rect.centery=150
pawnb2Count=0

pawnB3=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB3=pygame.transform.scale(pawnB3,(100,100))
pawnB3_rect=pawnB1.get_rect()
pawnB3_rect.centerx=250
pawnB3_rect.centery=150
pawnb3Count=0

pawnB4=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB4=pygame.transform.scale(pawnB4,(100,100))
pawnB4_rect=pawnB4.get_rect()
pawnB4_rect.centerx=350
pawnB4_rect.centery=150
pawnb4Count=0

pawnB5=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB5=pygame.transform.scale(pawnB5,(100,100))
pawnB5_rect=pawnB5.get_rect()
pawnB5_rect.centerx=450
pawnB5_rect.centery=150
pawnb5Count=0

pawnB6=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB6=pygame.transform.scale(pawnB6,(100,100))
pawnB6_rect=pawnB1.get_rect()
pawnB6_rect.centerx=550
pawnB6_rect.centery=150
pawnb6Count=0

pawnB7=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB7=pygame.transform.scale(pawnB7,(100,100))
pawnB7_rect=pawnB1.get_rect()
pawnB7_rect.centerx=650
pawnB7_rect.centery=150
pawnb7Count=0

pawnB8=pygame.image.load("./Pieces/black pawn.png").convert_alpha()
pawnB8=pygame.transform.scale(pawnB8,(100,100))
pawnB8_rect=pawnB1.get_rect()
pawnB8_rect.centerx=750
pawnB8_rect.centery=150
pawnb8Count=0

rookW1=pygame.image.load("./Pieces/white rook.png").convert_alpha()
rookW1=pygame.transform.scale(rookW1,(100,100))
rookW1_rect=rookW1.get_rect()
rookW1_rect.centerx=50
rookW1_rect.centery=750

knightW1=pygame.image.load("./Pieces/white knight.png").convert_alpha()
knightW1=pygame.transform.scale(knightW1,(100,100))
knightW1_rect=knightW1.get_rect()
knightW1_rect.centerx=150
knightW1_rect.centery=750

bishopW1=pygame.image.load("./Pieces/white bishop.png").convert_alpha()
bishopW1=pygame.transform.scale(bishopW1,(100,100))
bishopW1_rect=bishopW1.get_rect()
bishopW1_rect.centerx=250
bishopW1_rect.centery=750

queenW=pygame.image.load("./Pieces/white queen.png").convert_alpha()
queenW=pygame.transform.scale(queenW,(100,100))
queenW_rect=queenW.get_rect()
queenW_rect.centerx=350
queenW_rect.centery=750

kingW=pygame.image.load("./Pieces/white king.png").convert_alpha()
kingW=pygame.transform.scale(kingW,(100,100))
kingW_rect=kingW.get_rect()
kingW_rect.centerx=450
kingW_rect.centery=750

bishopW2=pygame.image.load("./Pieces/white bishop.png").convert_alpha()
bishopW2=pygame.transform.scale(bishopW2,(100,100))
bishopW2_rect=bishopW2.get_rect()
bishopW2_rect.centerx=550
bishopW2_rect.centery=750

knightW2=pygame.image.load("./Pieces/white knight.png").convert_alpha()
knightW2=pygame.transform.scale(knightW2,(100,100))
knightW2_rect=knightW2.get_rect()
knightW2_rect.centerx=650
knightW2_rect.centery=750


rookW2=pygame.image.load("./Pieces/white rook.png").convert_alpha()
rookW2=pygame.transform.scale(rookW2,(100,100))
rookW2_rect=rookW2.get_rect()
rookW2_rect.centerx=750
rookW2_rect.centery=750

pawnW1=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW1=pygame.transform.scale(pawnW1,(100,100))
pawnW1_rect=pawnW1.get_rect()
pawnW1_rect.centerx=50
pawnW1_rect.centery=650
pawnW1Count=0

pawnW2=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW2=pygame.transform.scale(pawnW2,(100,100))
pawnW2_rect=pawnW2.get_rect()
pawnW2_rect.centerx=150
pawnW2_rect.centery=650
pawnW2Count=0

pawnW3=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW3=pygame.transform.scale(pawnW3,(100,100))
pawnW3_rect=pawnW3.get_rect()
pawnW3_rect.centerx=250
pawnW3_rect.centery=650
pawnW3Count=0

pawnW4=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW4=pygame.transform.scale(pawnW4,(100,100))
pawnW4_rect=pawnW4.get_rect()
pawnW4_rect.centerx=350
pawnW4_rect.centery=650
pawnW4Count=0

pawnW5=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW5=pygame.transform.scale(pawnW5,(100,100))
pawnW5_rect=pawnW5.get_rect()
pawnW5_rect.centerx=450
pawnW5_rect.centery=650
pawnW5Count=0

pawnW6=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW6=pygame.transform.scale(pawnW6,(100,100))
pawnW6_rect=pawnW6.get_rect()
pawnW6_rect.centerx=550
pawnW6_rect.centery=650
pawnW6Count=0

pawnW7=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW7=pygame.transform.scale(pawnW7,(100,100))
pawnW7_rect=pawnW1.get_rect()
pawnW7_rect.centerx=650
pawnW7_rect.centery=650
pawnW7Count=0

pawnW8=pygame.image.load("./Pieces/white pawn.png").convert_alpha()
pawnW8=pygame.transform.scale(pawnW8,(100,100))
pawnW8_rect=pawnW1.get_rect()
pawnW8_rect.centerx=750
pawnW8_rect.centery=650
pawnW8Count=0
#All of the variables of all the pieces that will be used to blit the pieces on the screen
piecesToBlit=[rookB1,knightB1,bishopB1,queenB,kingB,bishopB2,knightB2,rookB2,
              pawnB1,pawnB2,pawnB3,pawnB4,pawnB5,pawnB6,pawnB7,pawnB8,
              rookW1,knightW1,bishopW1,queenW,kingW,bishopW2,knightW2,rookW2,
              pawnW1,pawnW2,pawnW3,pawnW4,pawnW5,pawnW6,pawnW7,pawnW8]
#Array of the rects of all the pieces on the board 

rectsToBlit=[rookB1_rect,knightB1_rect,bishopB1_rect,queenB_rect,kingB_rect,bishopB2_rect,knightB2_rect,rookB2_rect,
             pawnB1_rect,pawnB2_rect,pawnB3_rect,pawnB4_rect,pawnB5_rect,pawnB6_rect,pawnB7_rect,pawnB8_rect,
             rookW1_rect,knightW1_rect,bishopW1_rect,queenW_rect,kingW_rect,bishopW2_rect,knightW2_rect,rookW2_rect,
             pawnW1_rect,pawnW2_rect,pawnW3_rect,pawnW4_rect,pawnW5_rect,pawnW6_rect,pawnW7_rect,pawnW8_rect]
#Stores all the representation of all the pieces on the board 
compRepOfPieces=['bR','bN','bB','bQ','bK','bB2','bN2','bR2',
                 'bP1','bP2','bP3','bP4','bP5','bP6','bP7','bP8',
                 'wr','wn','wb','wq','wk','wb2','wn2','wr2',
                 'wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8']

allKings=[kingB_rect,kingW_rect]
allRooks=[rookB1_rect,rookB2_rect,rookW1_rect,rookW2_rect]
allQueens=[queenB_rect,queenW_rect]
allBishops=[bishopB1_rect,bishopB2_rect,bishopW1_rect,bishopW2_rect]
allKnights=[knightB1_rect,knightB2_rect,knightW1_rect,knightW2_rect]
allPawns=[pawnB1_rect,pawnB2_rect,pawnB3_rect,pawnB4_rect,pawnB5_rect,pawnB6_rect,pawnB7_rect,pawnB8_rect,
         pawnW1_rect,pawnW2_rect,pawnW3_rect,pawnW4_rect,pawnW5_rect,pawnW6_rect,pawnW7_rect,pawnW8_rect]

pawnMoveCounter=[pawnb1Count,pawnb2Count,pawnb3Count,pawnb4Count,pawnb5Count,pawnb6Count,pawnb7Count,pawnb8Count,
                 pawnW1Count,pawnW2Count,pawnW3Count,pawnW4Count,pawnW5Count,pawnW6Count,pawnW7Count,pawnW8Count]
