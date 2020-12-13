import pygame
import numpy as np
from gameboard import GameBoard
from notes import Notes
from deck import Deck
from player import Player

def rollDie():
    return np.random.randint(1,7)



if __name__ == "__main__":
    pygame.init()

    gameBoard = GameBoard("board_image.png")
    #gameBoard.setShowTiles(True)
    my_notes = Notes((gameBoard.size[0], 0))
    my_player = Player("mrs_peacock.png", (0, 5), gameBoard)
    screen = pygame.display.set_mode((gameBoard.size[0] + my_notes.size[0], max(gameBoard.size[1], my_notes.size[1])), pygame.DOUBLEBUF)

    clock = pygame.time.Clock()
    run = True
    num_moves = 1000#rollDie()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and num_moves > 0:
                    if my_player.moveLeft(gameBoard):
                        if my_player.getCurrentTile().type != "room" or my_player.getCurrentTile().type != "murder_room":
                            num_moves = num_moves - 1
                elif event.key == pygame.K_RIGHT and num_moves > 0:
                    if my_player.moveRight(gameBoard):
                        if my_player.getCurrentTile().type != "room" or my_player.getCurrentTile().type != "murder_room":
                            num_moves = num_moves - 1
                elif event.key == pygame.K_UP and num_moves > 0:
                    if my_player.moveUp(gameBoard):
                        if my_player.getCurrentTile().type != "room" or my_player.getCurrentTile().type != "murder_room":
                            num_moves = num_moves - 1
                elif event.key == pygame.K_DOWN and num_moves > 0:
                    if my_player.moveDown(gameBoard):
                        if my_player.getCurrentTile().type != "room" or my_player.getCurrentTile().type != "murder_room":
                            num_moves = num_moves - 1
                #check if player is out of movement
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in my_notes.buttonList:
                    if button.mouseOver(pygame.mouse.get_pos()):
                        button.toggleSelection()


        surface = gameBoard.getSurface()
        my_player.draw(surface, gameBoard)
        screen.blit(surface, (0, 0))
        for button in my_notes.buttonList:
            if button.mouseOver(pygame.mouse.get_pos()):
                button.toggleSelection
        my_notes.draw(screen)
        pygame.display.flip()
