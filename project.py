# https://matthewnewill.com/creating-a-chessboard-with-pygame/

import sys, pygame
from turtle import Screen, color
from pygame.locals import *
# from pygame.locals import(
#         MOUSEBUTTONUP,
#         K_ESCAPE,
#         KEYDOWN,
#         QUIT,
#     )
# pygame.init()
# SCREEN_WIDTH = 850
# SCREEN_HEIGHT = 850

# screen = pygame.display.set_mode((SCREEN_WIDTH, S))
# pygame.display.set_caption("Menu")

# run = True

# while run:
#     screen.fill((153, 102, 0))
#     for i in range(7):
#         for j in range(7):
#             pygame.draw.rect(screen, boardColour, pygame.Rect(100,100,400,400))
    
#     pygame.display.flip()
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

class Chess_Game():
    """
    This class basically runs the whole game
    
    """

    def __init__(self) -> None:
        pygame.init()
        background = pygame.image.load("fidel.jpg")
        SCREEN_WIDTH = 850
        SCREEN_HEIGHT = 850
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(background, [0,0])
    
    def Close_Game() -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

class Chess_Board(Chess_Game):
    """
    This class makes the board of the chess game

    """
    
    def __init__(self, chess_game) -> None:
        self.currentColor = [(255, 255, 255), (0,0,0)]
        for i in range(7):
            for j in range(7):
                pygame.draw.rect(chess_game.screen, self.currentColor[(i+j)%2], pygame.Rect(100+125*j,100+125*i,125+125*j,125+125*i))

class Chess_Piece():
    """
    This class makes the chess pieces do stuff

    """
    def __init__(self) -> None:
        self.displayImage

    def drawPiece(image) -> None:
        self.display
        pass

    def takePiece() -> None:
        pass


class Pawn(Chess_Piece):
    """
    This class implements the pawn piece (Chaff infantry)

    """


class King(Chess_Piece):
    """
    This class implements the king piece (Legendary lord) 

    """

class Queen(Chess_Piece):
    """
    This class implements the queen piece (Hero)

    """

class Bishop(Chess_Piece):
    """
    This class implements the bishop piece (Mage)

    """

class Knight(Chess_Piece):
    """
    This class implements the knight piece (Cavalry)
    
    """
    def __init__(self) -> None:
        super()
        displayImage = pygame.image.load("Chess_Horse.jpg")

class Rook(Chess_Piece):
    """
    This class implements the rook piece ()
    
    """
