import pygame

class Player:
    def __init__(self, imageFile, position, tileDim): #position is per board grid, tileDim comes from GameBoard.Tile.dimensions
        playerImage = pygame.image.load(imageFile)
        self.surface = pygame.Surface(tileDim, pygame.SRCALPHA)
        self.surface.blit(playerImage, (0, 0))
        self.tileDim = tileDim
        self.setPosition(position)

    def draw(self, surface, board): #surface should come directly from the board? probably.
        surface.blit(self.surface, self.boardPosition)
        return surface

    def setPosition(self, position): #position is on the grid
        self.position = position
        positionX = self.position[0] * self.tileDim[0] + self.tileDim[0] / 2
        positionY = self.position[1] * self.tileDim[1] + self.tileDim[1] / 2
        self.boardPosition = (positionX, positionY)

    def getPosition(self):
        return self.position