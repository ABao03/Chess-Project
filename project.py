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
        self.SCREEN_WIDTH = 850
        self.SCREEN_HEIGHT = 850
        self.thisScreen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.draw.rect(self.thisScreen, (255, 225, 219), pygame.Rect(0,0,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)) 
    
    def Close_Game() -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

class Chess_Piece(Chess_Game):
    """
    This class makes the chess pieces do stuff

    """

    def __init__(self, chess_game) -> None:
        self.thisScreen = chess_game.screen

    def drawPiece(self, x, y) -> pygame.image:
        self.xCoord = x
        self.yCoord = y

        self.screen.blit(self.thisImage, (x,y))

    def takePiece() -> None:
        pass

class Chess_Board(Chess_Game):
    """
    This class makes the board of the chess game. Board is simulated in a matrix

    """
    
    def __init__(self, chess_game) -> None:
        self.boardMap = {}
        self.currentColor = [(255, 255, 255), (0,0,0)]
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(chess_game.thisScreen, self.currentColor[(i+j)%2], pygame.Rect(50+95*j,50+95*i,95,95)) 
                # boardMap.add(i, j)

class Pawn(Chess_Piece, Chess_Board, Chess_Game): 
    """
    This class implements the pawn piece (Chaff infantry)

    """

    def __init__(self, game) -> None:
        super()
        self.screen = game.thisScreen
        self.thisImage = pygame.image.load("pawn.jpg")
        self.thisImage = pygame.transform.scale(self.thisImage, (95, 95)) 


class King(Chess_Piece, Chess_Board, Chess_Game):
    """
    This class implements the king piece (Legendary lord) 

    """
    def __init__(self, game) -> None:
        super()
        self.screen = game.thisScreen
        self.thisImage = pygame.image.load("king.jpg")
        self.thisImage = pygame.transform.scale(self.thisImage, (95, 95))

class Queen(Chess_Piece, Chess_Board, Chess_Game):
    """
    This class implements the queen piece (Hero)

    """
    def __init__(self, game) -> None:
        super()
        self.screen = game.thisScreen
        self.thisImage = pygame.image.load("queen.jpg")
        self.thisImage = pygame.transform.scale(self.thisImage, (95, 95))

class Bishop(Chess_Piece, Chess_Board, Chess_Game): 
    """
    This class implements the bishop piece (Mage)

    """
    def __init__(self, game) -> None:
            super()
            self.screen = game.thisScreen
            self.thisImage = pygame.image.load("bishop.jpg")
            self.thisImage = pygame.transform.scale(self.thisImage, (95, 95))

class Knight(Chess_Piece, Chess_Board, Chess_Game):
    """
    This class implements the knight piece (Cavalry)
    
    """
        # def __init__(self, chess_game) -> None:
        # self.currentColor = [(255, 255, 255), (0,0,0)] 
        # for i in range(8): 
        #     for j in range(8):
        #         pygame.draw.rect(chess_game.thisScreen, self.currentColor[(i+j)%2], pygame.Rect(50+95*j,50+95*i,95,95)) 

    def __init__(self, game) -> None:
        super()
        self.screen = game.thisScreen
        self.thisImage = pygame.image.load("knight.jpg")
        self.thisImage = pygame.transform.scale(self.thisImage, (95, 95))

class Rook(Chess_Piece, Chess_Board, Chess_Game):
    """
    This class implements the rook piece (Siege Tower)
    
    """
    def __init__(self, game) -> None:
        super()
        self.screen = game.thisScreen
        self.thisImage = pygame.image.load("rook.jpg")
        self.thisImage = pygame.transform.scale(self.thisImage, (95, 95))

class TakenPieces():
    """
    This class displays the game's casualties

    """

class Timer():
    """
    This class displays the time passed when each black and white take their turn to choose their move 

    """
