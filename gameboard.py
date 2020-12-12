#!/bin/python3
# file: gameboard.py
import numpy as np
import pygame

class GameBoard:
    class Tile:
        colors = {
            "hallway": (0, 150, 150, 150),
            "unavailable": (0, 0, 0, 200),
            "start_position": (100, 200, 0, 150),
            "room": (100, 0, 200, 150),
            "murder_room": (255, 0, 0, 150),
            "door": (0, 0, 255, 150)
        }

        dimensions = (0.0, 0.0)
        initialOffset = (0.0, 0.0)

        def __init__(self, tileType, position):
            self.type = tileType
            self.position = position
        
        def draw(self, surface):
            pygame.draw.rect(surface, GameBoard.Tile.colors[self.type], self.position)
            return surface
        
        def canBeMovedTo(self, fromSpace):
            if self.type != "unavailable":
                return True
                # if self.type == "hallway" or self.type == "start_position" or self.type == "door":
                #     return True
                # elif self.type == "room" or self.type == "murder_room":
                #     if fromSpace.type == "door":
                #         return True     
                #     else:
                #         return False
            else:
                return False

    def __init__(self, imageFilename):
        self.showTiles = False
        #get board data from files
        boardImage = pygame.image.load(imageFilename)
        dataFile = imageFilename[0:imageFilename.find('.')] + "_data.txt"
        self.parse_grid_positions(dataFile)

        #setup board surfaces
        self.size = boardImage.get_size()
        self.boardSurface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.tileSurface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.boardSurface.blit(boardImage, (0, 0))


    def parse_grid_positions(self, filename):
        with open(filename, 'r') as f:
            w, h = [int(x) for x in next(f).split()]
            self.gridSize = (w,h)
            i = 0
            tileArray = np.zeros((w,h), dtype = (float, 4))
            tileTypeList = []

            for i in range(w * h * 2):
                line = next(f)
                if (i + 1) % 2:
                    tileTypeList.append(line[0:len(line)-1])
                else:
                    j = i // 2
                    positions = [float(x) for x in line.split()]
                    index = self._get2DIndex(j)
                    tileArray[index[0], index[1]] = tuple(positions)

            self.tileList = []
            for j in range(0, len(tileTypeList)):
                el = tileTypeList[j]
                index = self._get2DIndex(j)
                pos = tileArray[index[0], index[1]]
                tile = GameBoard.Tile(el, pos)
                self.tileList.append(tile)
            GameBoard.Tile.initialOffset = (self.tileList[0].position[0], self.tileList[0].position[1])
            GameBoard.Tile.dimensions = (self.tileList[0].position[2], self.tileList[0].position[3])

    def _getIndex(self, twoDIndex):
        return twoDIndex[0] + self.gridSize[0] * twoDIndex[1]
            
    def _get2DIndex(self, index):
        return (index // self.gridSize[0], index % self.gridSize[0])

    def setShowTiles(self, val):
        self.showTiles = val

    def draw(self, screen):
        screen.blit(self.boardSurface, (0, 0))
        if (self.showTiles):
            self.tileSurface.fill((0, 0, 0, 0))
            for tile in self.tileList:
                tile.draw(self.tileSurface)
            screen.blit(self.tileSurface, (0, 0))
        return screen

    def getSurface(self):
        surface = pygame.Surface(self.size, pygame.SRCALPHA)
        return self.draw(surface)



            
