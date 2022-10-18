from project import Chess_Game, Chess_Board
import pygame, sys
from pygame.locals import *


run = True
while run:
    
    thisGame = Chess_Game()
    thisBoard = Chess_Board(thisGame)
    pygame.display.update()
    Chess_Game.Close_Game()
