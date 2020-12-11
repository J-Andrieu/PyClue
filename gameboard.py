#!/bin/python3
# file: gameboard.py
import numpy as np
import pygame

class GameBoard:
    def __init__(self, image: pygame.image, gridSize):
        #set up board window and image
        self.boardImage = image
        self.size = image.size
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(image, (0, 0))
        
        #initialize board grid
        #we've seen both 22 and 25
        self.grid = np.array([gridSize[0], gridSize[1]])
        self.x_step = self.size[0] / gridSize[0]
        self.y_step = self.size[1] / gridSize[1]

        #

        
