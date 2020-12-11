import pygame
import numpy as np

pygame.init()

filename = input("What file?? ")
#set up board window and image
boardImage = pygame.image.load(filename)
size = boardImage.get_size()
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
buttonSurface = pygame.Surface(size, pygame.SRCALPHA)
buttonSurface.fill((0, 0, 0, 0))
screen.blit(boardImage, (0, 0))
pygame.display.update()


#initialize board grid
#we've seen both 22 and 25
gridSize = eval(input("What size is the board? ")) #pls pass me a tuple
grid = np.zeros(shape=gridSize)
x_step = size[0] / gridSize[0]
y_step = size[1] / gridSize[1]

for ix,iy in np.ndindex(grid.shape):
    pygame.draw.rect(buttonSurface, (0, 150, 150, 150), (ix * x_step, iy * y_step, x_step, y_step))
screen.blit(buttonSurface, (0, 0))

pygame.display.update()
input()