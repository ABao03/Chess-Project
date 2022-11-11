from project import *
import pygame
from pygame.locals import *


run = True
while run:
    
    thisGame = Chess_Game()
    thisBoard = Chess_Board(thisGame)
    
    Chess_Game.Close_Game() 

    topPawns = list()
    botPawns = list()

    for i in range(8):
        topPawns.append(Pawn(thisGame))
        botPawns.append(Pawn(thisGame))
        topPawns[i].drawTops(50 + i * 95, 100)
        botPawns[i].drawBots(50 + i * 95, 605) 

    topLeftKnight = Knight(thisGame)
    topLeftKnight.drawTops(150, 50)

    bottomLeftKnight = Knight(thisGame)
    bottomLeftKnight.drawBots(150, 650)

    topRightKnight = Knight(thisGame)
    topRightKnight.drawTops(600, 50)
    
    bottomRightKnight = Knight(thisGame)
    bottomRightKnight.drawBots(600, 650)
    
    topBishops = list()
    botBishops = list()

    for i in range(2):
        topBishops.append(Bishop(thisGame))
        botBishops.append(Bishop(thisGame))
        topBishops[i].drawTops(145 + i * 380, 50)
        botBishops[i].drawBots(145 + i * 380, 605)

    topRooks = list()
    botRooks = list()
    for i in range(2):
        topRooks.append(Rook(thisGame))
        botRooks.append(Rook(thisGame))
        topRooks[i].drawTops(50 + i * 650, 50)
        botRooks[i].drawBots(50 + i * 650, 700)

    topKing = King(thisGame)
    topKing.drawTops(450, 50)

    botKing = King(thisGame)
    botKing.drawBots(450, 700)

    pygame.display.update() # ALWAYS KEEP THIS AT THE END

    
