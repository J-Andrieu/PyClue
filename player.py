import pygame

class Player:
    def __init__(self, imageFile, position, gameBoard): #position is per board grid, tileDim comes from GameBoard.Tile.dimensions
        playerImage = pygame.image.load(imageFile)
        self.surface = pygame.Surface(gameBoard.Tile.dimensions, pygame.SRCALPHA)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(pygame.transform.scale(playerImage, (int(gameBoard.Tile.dimensions[0]), int(gameBoard.Tile.dimensions[1]))), (0, 0))
        self.gameBoard = gameBoard
        self.tileDim = gameBoard.Tile.dimensions
        self.initialOffset = gameBoard.Tile.initialOffset
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
        try:
            nextPos = (self.position[1], self.position[0] - 1)
            nextPosTile = gameBoard.tileList[gameBoard._getIndex(nextPos)]

            currentPos = ((self.position[1], self.position[0]))
            currentPosTile = gameBoard.tileList[gameBoard._getIndex(currentPos)]

            #print(f"to: {nextPosTile.type}, from: {currentPosTile.type}")
            if nextPosTile.canBeMovedTo(currentPosTile):
                self.setPosition((nextPos[1], nextPos[0]))
                return True

        except Exception as e:
            #print(f"oof: {e}")
            return False

        return False
    
    def moveRight(self, gameBoard):
        try:
            nextPos = (self.position[1], self.position[0] + 1)
            nextPosTile = gameBoard.tileList[gameBoard._getIndex(nextPos)]

            currentPos = ((self.position[1], self.position[0]))
            currentPosTile = gameBoard.tileList[gameBoard._getIndex(currentPos)]

            #print(f"to: {nextPosTile.type}, from: {currentPosTile.type}")
            if nextPosTile.canBeMovedTo(currentPosTile):
                self.setPosition((nextPos[1], nextPos[0]))
                return True

        except Exception as e:
            #print(f"oof: {e}")
            return False

        return False

    def getCurrentTile(self):
        currentPos = ((self.position[1], self.position[0]))
        return self.gameBoard.tileList[self.gameBoard._getIndex(currentPos)]

    def moveUp(self, gameBoard):
        try:
            nextPos = (self.position[1] - 1, self.position[0])
            nextPosTile = gameBoard.tileList[gameBoard._getIndex(nextPos)]

            currentPos = ((self.position[1], self.position[0]))
            currentPosTile = gameBoard.tileList[gameBoard._getIndex(currentPos)]

            #print(f"to: {nextPosTile.type}, from: {currentPosTile.type}")
            if nextPosTile.canBeMovedTo(currentPosTile):
                self.setPosition((nextPos[1], nextPos[0]))
                return True

        except Exception as e:
            #print(f"oof: {e}")
            return False

        return False

    def moveDown(self, gameBoard):
        try:
            nextPos = (self.position[1] + 1, self.position[0])
            nextPosTile = gameBoard.tileList[gameBoard._getIndex(nextPos)]

            currentPos = ((self.position[1], self.position[0]))
            currentPosTile = gameBoard.tileList[gameBoard._getIndex(currentPos)]

            #print(f"to: {nextPosTile.type}, from: {currentPosTile.type}")
            if nextPosTile.canBeMovedTo(currentPosTile):
                self.setPosition((nextPos[1], nextPos[0]))
                return True

        except Exception as e:
            #print(f"oof: {e}")
            return False

        return False
        