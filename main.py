from project import Chess_Game, Chess_Board, Chess_Piece, Knight, Pawn
import pygame
from pygame.locals import *


run = True
while run:
    
    thisGame = Chess_Game()
    thisBoard = Chess_Board(thisGame)
    
    Chess_Game.Close_Game() 

    topLeftPawn = Pawn(thisGame)
    topLeftPawn.drawPiece(50, 50)

    topLeftKnight = Knight(thisGame)
    topLeftKnight.drawPiece(150, 50)

    bottomLeftKnight = Knight(thisGame)
    bottomLeftKnight.drawPiece(150, 650)

    topRightKnight = Knight(thisGame)
    topRightKnight.drawPiece(600, 50)
    
    bottomRightKnight = Knight(thisGame)
    bottomRightKnight.drawPiece(600, 650)
    
    
    
    pygame.display.update() # ALWAYS KEEP THIS AT THE END

    
