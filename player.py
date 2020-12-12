import pygame

class Player:
    def __init__(self, imageFile, position, tileDim, tileOffset): #position is per board grid, tileDim comes from GameBoard.Tile.dimensions
        playerImage = pygame.image.load(imageFile)
        self.surface = pygame.Surface(tileDim, pygame.SRCALPHA)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(pygame.transform.scale(playerImage, (int(tileDim[0]), int(tileDim[1]))), (0, 0))
        self.tileDim = tileDim
        self.initialOffset = tileOffset
        self.setPosition(position)
        self.hand = []

    def draw(self, surface, board): #surface should come directly from the board? probably.
        surface.blit(self.surface, self.boardPosition)
        return surface

    def setPosition(self, position): #position is on the grid
        self.position = position
        positionX = self.position[0] * (self.tileDim[0] + 1) + self.initialOffset[0]
        positionY = self.position[1] * (self.tileDim[1] + 1) + self.initialOffset[1]
        self.boardPosition = (positionX, positionY)

    def getPosition(self):
        return self.position

    def addToHand(self, card):
        self.hand.append(card)
        
    def moveLeft(self, gameBoard):
        if gameBoard.tileList[gameBoard._getIndex(self.position)].canBeMovedTo():
            self.setPosition((self.position[0]-1,self.position[1]))
    
    def moveRight(self, gameBoard):
        if gameBoard.tileList[gameBoard._getIndex(self.position)].canBeMovedTo():
            self.setPosition((self.position[0]+1,self.position[1]))


    def moveUp(self, gameBoard):
        if gameBoard.tileList[gameBoard._getIndex(self.position)].canBeMovedTo():
            self.setPosition((self.position[0],self.position[1]-1))

    def moveDown(self,  gameBoard):
        if gameBoard.tileList[gameBoard._getIndex(self.position)].canBeMovedTo():
            self.setPosition((self.position[0],self.position[1]+1))

        